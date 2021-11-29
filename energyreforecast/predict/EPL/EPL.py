import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import os
import seaborn as sns


# y = mx + b
# m = 0.1083
# b = 27.261

class EnergyPredict:
	GRAPH_PATH = "predict/static/graph"

	def __init__(self, dateIn, dateOut, production, workingday, allocate, saving, zone="", monthpredict=1, debug=False):
		self.dateIn					= dateIn
		self.dateOut				= dateOut
		self.production			= production
		self.workingday			= workingday
		self.allocate				= allocate
		self.saving					= saving
		self.zone						= zone
		self.monthpredict		= monthpredict
		self.debug					= debug
		self.sql_host				= "127.0.0.1"
		self.sql_user				= "root"
		self.sql_pwd				= ""
		self.sqlEngine      = create_engine(f"mysql+pymysql://{self.sql_user}:{self.sql_pwd}@{self.sql_host}", pool_recycle=3600)
		os.makedirs(self.GRAPH_PATH, exist_ok=True)
		self.dbConnection   = self.sqlEngine.connect()
		self.fetchdata()																												#FETCH DB
		self.var = {}
		self.fix = {}
		self.techratio = {}
		self.MWh_day = {}
		self.energyvar = {}
		self.energyfix = {}
		self.energypredict = {}
		self.beforesaving = {}
		self.aftersaving = {}
		self.RecID = self.savedb()																				#SAVE DB
		self.linear = self.df.groupby(["name_machine"]).apply(self.calc)										#CALC
		self.dbConnection.close()

		for x in self.linear.keys():
			var = self.production * self.linear[x][0]															#var
			self.var[x] = var
			fix = self.workingday * self.linear[x][1]															#fix
			self.fix[x] = fix
			energyvar = var * self.techratio[x]											                       	#energy var
			self.energyvar[x] = energyvar
			energyfix = fix * self.MWh_day[x]																	#energy fix
			self.energyfix[x] = energyfix
			energypredict = (energyvar + energyfix)
			self.energypredict[x] = energypredict																#energy predict
			self.beforesaving[x] = energypredict																#before saving
			self.aftersaving[x] = energypredict * ((100 - self.saving) / 100) * ((100 - self.allocate) / 100)						#after saving

		if self.debug:
			
			print("\nLinear Regression")
			for x in self.linear.keys():
				print(f"y = {self.linear[x][0]:0.2f} x + {self.linear[x][1]:0.2f} : (R2={self.linear[x][2]:0.2f})")
			print("\ntech ratio")
			for x in self.techratio:
				print(f"{x} : {self.techratio[x]:0.2f}")
			print("\nvar")
			for x in self.var:
				print(f"{x} : {self.var[x]:0.2f}")
			print("\nenergy var")
			for x in self.energyvar:
				print(f"{x} : {self.energyvar[x]:0.2f}")
			print("\nfix")
			for x in self.fix:
				print(f"{x} : {self.fix[x]:0.2f}")
			print("\nenergy fix")
			for x in self.energyfix:
				print(f"{x} : {self.energyfix[x]:0.2f}")
			print("\nenergy predict")
			for x in self.energypredict:
				print(f"{x} : {self.energypredict[x]:0.2f}")
			print("\nbefore saving")
			for x in self.beforesaving:
				print(f"{x} : {self.beforesaving[x]:0.2f}")
			print("\nafter saving")
			for x in self.aftersaving:
				print(f"{x} : {self.aftersaving[x]:0.2f}")
			print("\n")

	def fetchdata(self):
		where = ""
		if self.zone != "":
			where = f" and name_machine='{self.zone}'"
		self.df = pd.read_sql(f"select * from energyreforecast.predict_daily where date between '{self.dateIn}' and '{self.dateOut}' {where}", self.dbConnection)
		pd.set_option('display.expand_frame_repr', False)
		return self.df

	def calc(self, delta):	                                                                            #groupby func
		X = delta.iloc[:, 3].values.reshape(-1, 1)													    #production field
		Y = delta.iloc[:, 4].values.reshape(-1, 1)													    #energy field
		name = delta["name_machine"].values[0]
		#X[-1] = last production
		#Y[-1] = last energy
		self.techratio[name] = float(Y[-1] / X[-1])														#tech_ratio
		self.MWh_day[name] = float(Y[-1] / self.workingday)										        #MWh_day
		linear_regressor = LinearRegression()
		y_pred = linear_regressor.fit(X, Y).predict(X)
		m = linear_regressor.coef_[0][0]
		b = linear_regressor.intercept_[0]
		R = linear_regressor.score(X, Y)
		sns.set()
		plt.scatter(X, Y, color='g' , alpha=0.9)
		plt.xlabel("Production (Ton)", fontsize=9)
		plt.ylabel("Energy (MWh)", fontsize=9)
		plt.plot(X, y_pred, color="purple", label=" y={:.2f}x+{:.2f} \n R2={:.2f}".format(m, b, R))
		plt.legend(fontsize=9)
		figure = plt.gcf()
		figure.set_size_inches(10,4.5)
		plt.savefig(self.GRAPH_PATH + "/" + str(self.RecID) + "_" + name + ".png", dpi=100)
		plt.close()
		return m, b, R				# m b R2
	
	def savedb(self):
		cursor = self.dbConnection.execute(f"insert into energyreforecast.predict_graph(graph_datein, graph_dateout, graph_production, graph_workingday, graph_allocate, graph_saving, graph_zone, graph_monthpredict ) values('{self.dateIn}', '{self.dateOut}', {self.production}, {self.workingday}, {self.allocate}, {self.saving}, '{self.zone}', {self.monthpredict} )")
		return cursor.lastrowid
	

if __name__ == "__main__":
	print("Energy Predict Library")
	# EnergyPredict(dateIn="2021-01-01", dateOut="2021-03-31", production=2200, workingday=30, allocate=1, saving=3, zone="", debug=True)