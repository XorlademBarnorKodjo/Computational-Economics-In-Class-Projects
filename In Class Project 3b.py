#!/usr/bin/env python
# coding: utf-8

# In[1]:


dct = {}
dct


# In[2]:


dct = {"run":{},
      "walk":{}}

dct


# In[3]:


dct = {"run":"to move swiftly by foot",
      "walk":"to move slowly or leisurely by foot"}

dct


# In[4]:


dct = {"run":{
    "verb":"to move swiftly by foot",
    "noun":"a period of time while one was running"},
       "walk":{
    "verb":"to move slowly by foot",
    "noun":"a period of time while one was walking"}
      }

dct


# In[5]:


import pandas as pd
pd.DataFrame(dct)


# In[6]:


import pandas as pd
df = pd.DataFrame(dct)
df


# In[7]:


# call a column in the df
df["run"]


# In[8]:


# call a row in the df
df.loc["verb"]


# In[9]:


# call a particular cell
df.loc["verb", "run"]


# In[10]:


dct = {"Caden":{"Age":19,
                "Interesting fact":"Played hockey"},
      "Jacob P":{"Age":21,
                "Interesting fact":"Dr caton got name wrong"},
      "Genesis":{"Age":21,
                "Interesting fact":"Wrestled in highschool"},
      "Sam":{"Age":20,
                "Interesting fact":"Tore ACL"},
      "Proma":{"Age":24,
                "Interesting fact":"Learned Classics"},
      "Zach":{"Age":20,
                "Interesting fact":"Track and Field Team"},
      "Jacob K":{"Age":20,
                "Interesting fact":"Played Classics"},
       "Brabdon":{"Age":20,
                "Interesting fact":"Played baseball"},
      "Gabe":{"Age":20,
                "Interesting fact":"Double major"},
      "Drew":{"Age":49,
                "Interesting fact":"A veteran"},
      "Isaac":{"Age":21,
                "Interesting fact":"Travelling to Europe"},
      "Kodjo":{"Age":30,
                "Interesting fact":"Wife Soldier"}}

dct


# In[11]:


#transpose a dataframe by calling df.T
pd.DataFrame(dct).T


# In[12]:


dct["Dr. Caton"] = {}
dct["Dr. Caton"]["Age"] = None
dct["Dr. Caton"]["Interesting fact"] = "I used to ride dirtbikes"

dct


# In[13]:


dct["Joe Biden"] = {"Age":78,
                   "Interesting fact": "Plays mario Kart"}


# In[14]:


pd.DataFrame(dct).T


# In[15]:


faculty_dict =  {"William Nganje":{"Website":"https://www.ndsu.edu/agecon/faculty/william_nganje/#c622350", 
                                     "Areas of Specialization":"Risk management; financial analysis; economics of obesity, food safety and food terrorism; experimental economics; and consumer choice theory",
                                     "Bio":"NA"},
                 "David Bullock": {"Website":"https://www.ndsu.edu/agecon/faculty/bullock/#c622728",
                                    "Areas of Specialization": "futures and options markets, over-the-counter derivatives, trading, risk management, agrifinance, Monte Carlo simulation, and Big Data",
                                    "Bio":"Dr. David W. Bullock is a Research Associate Professor affiliated with the Center for Trading and Risk at NDSU.  His research interests include futures and options markets, over-the-counter derivatives, trading, risk management, agrifinance, Monte Carlo simulation, and Big Data applications in agriculture.  His academic research in option portfolio theory has been published in both the Journal of Economics and Business and the International Review of Economics and Finance.  Additionally, he was the primary contributor behind the AgriBank Insights publication series which won a National AgriMarketing Association (NAMA) award for the best company publication in 2016. Before coming to NDSU in January 2018, Dr. Bullock held numerous positions for over 25 years in the government and private sectors including the Senior Economist at AgriBank FCB – the regional Farm Credit System funding bank for the Upper Midwest region, Director of Research and Senior Foods Economist at Fortune 500 commodity risk management firm INTL FCStone Inc., the Senior Dairy Analyst at Informa Economics, a Risk Management Specialist with the Minnesota Department of Agriculture, and the Senior Economist at the Minneapolis Grain Exchange. David began his academic career as an Assistant Professor and Extension Marketing Economist at Montana State University after graduating from Iowa State University with a Ph.D. in agricultural economics with fields in agricultural price analysis and econometrics in 1989.  Prior to entering ISU, he received bachelor’s (1982) and master’s (1984) degrees in agricultural economics from Northwest Missouri State University. Dr. Bullock is originally from the small northwestern Missouri farming community of Lathrop which is located 40 miles north of the Kansas City metropolitan area.  While in high school, he served as a regional state Vice-President in the Future Farmers of America (FFA) during his senior year."},
                 "James Caton": {"Website":"https://www.ndsu.edu/centers/pcpe/about/directory/james_caton/",
                                 "Areas of Specialization": "Entrepreneurship, Institutions, Macroeconomics, Computation",
                                 "Bio":"James Caton is a faculty fellow at the NDSU Center for the Study of Public Choice and Private Enterprise (PCPE) and an assistant professor in the NDSU Department of Agribusiness and Applied Economics. He teaches undergraduate courses in the areas of macroeconomics, international trade, and computation. He specializes in research related to entrepreneurship, agent-based computational economics, market process theory, and monetary economics. His research has been published in the Southern Economic Journal, Erasmus Journal for Philosophy and Economics, Journal of Entrepreneurship and Public Policy and other academic publications. He co-edited Macroeconomics, a two volume set of essays and primary sources that represent the core of macroeconomic thought. He is also a regular contributor to the American Institute for Economic Research's Sound Money Project, which conducts research and promotes awareness about monetary stability and financial privacy. He resides in Fargo with his wife, Ingrid, and their children."},
                 "David Englund": {"Website":"https://www.ndsu.edu/agecon/faculty/englund/#c622903",
                                 "Areas of Specialization": "Teaches Economic Principles, Led NDSU NAMA to National Champions",
                                 "Bio":"David Englund is a lecturer in the department.  He came to the department with 16 years of teaching experience, having taught Principles of Microeconomics, Principles of Macroeconomics, Money and Banking, Consumer Behavior, Selected Topics in Business, and several other classes.  He also had 10 years’ experience advising student NAMA chapters, having been awarded the Outstanding Advisor of the Year for a Developing Chapter in 2002, and the Outstanding Advisor of the Year award in 2009.\nDavid primarily teaches Survey of Economics, Principles of Microeconomics, Skills for Academic Success, Agricultural Marketing, and NAMA (co-teaches).  He joined the NAMA team in the 2014-2015 school year as a co-advisor and helped coach the student team to a 3rd place finish in the national student marketing plan competition at the national conference.\nSome of David’s outside interests are jogging, photography, and writing fiction novels.  His latest release, Camouflaged Encounters has received positive reviews."},
                 "Erik Hanson": {"Website":"https://www.ndsu.edu/agecon/faculty/hanson/#c622905",
                                 "Areas of Specialization": "Ag Management, Ag Finance",
                                 "Bio":"Erik Hanson is an Assistant Professor in the Department of Agricultural and Applied Economics. He teaches courses on agribusiness management and agricultural finance. Erik completed his Ph.D. at the University of Minnesota in 2016. Prior to that, Erik completed a master’s degree at the University of Illinois (2013) and a bachelor’s degree at Minnesota State University Moorhead (2011)."},
                 "Ronald Haugen": {"Website":"https://www.ndsu.edu/agecon/about_us/faculty/ron_haugen/#c654700",
                                 "Areas of Specialization": "Extension Farm Management Specialist",
                                 "Bio":"Ron Haugen is an Extension Farm Management Specialist. He has been in the department since 1991. Farm management topics include: crop budgets, crop insurance, farm programs, custom farm rates, land rents, machinery economics, commodity price projections and agricultural income taxes. He computes the North Dakota Land Valuation Model."},
                 "Robert Hearne": {"Website":"https://www.ndsu.edu/agecon/faculty/hearne/#c622909",
                                 "Areas of Specialization": "water resources management institutions, water markets, protected area management, and the economic valuation of environmental goods and services",
                                 "Bio":"Dr. Bob Hearne has been in the Department of Agribusiness and Applied Economics since 2002.   His research focuses on water resources management institutions, water markets, protected area management, and the economic valuation of environmental goods and services.  He has professional experience in Europe, Asia, Latin America, and Asia. "},
                 "Jeremy Jackson": {"Website":"https://www.ndsu.edu/centers/pcpe/about/directory/jeremy_jackson/",
                                 "Areas of Specialization": "public choice and the political economy; the social consequences of economic freedom; happiness and well-being; and philanthropy and nonprofits",
                                 "Bio":"Jeremy Jackson is director of the Center for the Study of Public Choice and Private Enterprise, scholar at the Challey Institute for Global Innovation and Growth, and professor of economics in the Department of Agribusiness and Applied Economics at North Dakota State University.. He teaches undergraduate and graduate courses in the areas of microeconomics, public economics, and game theory and strategy. His research covers diverse topics, including public choice and the political economy; the social consequences of economic freedom; happiness and well-being; and philanthropy and nonprofits. His research has been published in Applied Economics, The Independent Review, Public Choice, Contemporary Economic Policy, Journal of Happiness Studies, and other refereed and non-refereed sources"},
                 "Prithviraj Lakkakula": {"Website":"https://www.ndsu.edu/agecon/faculty/prithviraj_lakkakula/#c623441",
                                 "Areas of Specialization": "Agricultural Price Analysis",
                                 "Bio":"Prithviraj has a Ph.D. Food and Resource Economics, University of Florida, 2014, an M.S. Agricultural Economics, University of Arkansas, 2010 and a B.Sc. Agriculture, Acharya N.G Ranga Agricultural University, Hyderabad, 2007. He teaches ECON 341: Intermediate Microeconomics and AGEC 344: Agricultural Price Analysis"},
                 "Siew Lim": {"Website":"https://www.ndsu.edu/agecon/faculty/lim/#c624837",
                                 "Areas of Specialization": "applied microeconomics, production economics, industrial organization, transportation and regional development",
                                 "Bio":"Siew Hoon Lim is an associate professor of economics. Her current research is in applied microeconomics, production economics, industrial organization, transportation and regional development. Her recent research works include transportation and  regional development"},
                 "Raymond March": {"Website":"https://www.ndsu.edu/centers/pcpe/about/directory/raymond_march/",
                                 "Areas of Specialization": "public and private provision and governance of health care",
                                 "Bio":"Raymond March is a scholar at the Challey Institute for Global Innovation and Growth with the Center for the Study of Public Choice and Private Enterprise and an assistant professor of economics in the Department of Agribusiness and Applied Economics at North Dakota State University. He teaches courses in microeconomics, the history of economic thought, and health economics. His research examines the public and private provision and governance of health care in the United States, particularly in pharmaceutical markets. His research has appeared in Southern Economic Journal, Public Choice, Research Policy, Journal of Institutional Economics, and other academic publications. His popular writings are published in the Washington Examiner, The Hill, Real Clear Health, Health Care News, Sun Sentinel, Foundation for Economic Education, and elsewhere. Raymond is also a research fellow at the Independent Institute and the director of FDAReview.org, an educational research and communications project on the U.S. Food and Drug Administration (FDA). He regularly blogs on health policy at The Beacon. Raymond resides in Fargo with his wife, Amy, daughter Tinsley, son Grant, and two ill-behaved cat."},
                 "Dragan Miljkovic": {"Website":"https://www.ndsu.edu/agecon/faculty/miljkovic/#c625001",
                                 "Areas of Specialization": "Dragan Miljkovic is professor of agricultural economics in the Department of Agribusiness & Applied Economics at North Dakota State University. Dr. Miljkovic holds B.S. and M.S. degrees in Economics from the University of Belgrade, and Ph.D. in Agricultural Economics from the University of Illinois at Urbana-Champaign. Research areas of interest include agricultural price analysis, international economics, and agricultural and food policy including human nutrition, obesity, and food safety. Dr. Miljkovic authored over sixty peer reviewed journal articles and book chapters, and edited three books. He has more than 60 selected and invited presentations at various domestic and international conferences and universities in North America, Europe, New Zealand, and Australia. Dr. Miljkovic teaches undergraduate class in agricultural prices and graduate advanced econometrics class. Dr. Miljkovic is the Founding Editor and Editor-In-Chief of the Journal of International Agricultural Trade and Development (JIATD), and has also served as the Associate Editor of the Journal of Agricultural and Applied Economics (JAAE). He is an active member of numerous professional organizations and associations including the International Agricultural Trade Research Consortium (IATRC), the AAEA, the SAEA, WAEA, NAREA, AARES, and regional projects NCCC-134, WERA-72, and S-1016.",
                                 "Bio":"agricultural price analysis, international economics, and agricultural and food policy including human nutrition, obesity, and food safety"},
                 "Frayne Olson": {"Website":"https://www.ndsu.edu/agecon/faculty/olson/#c625016",
                                 "Areas of Specialization": "Crop Economist/Marketing",
                                 "Bio":"Dr. Frayne Olson is the Crop Economist/Marketing Specialist with the North Dakota State University Extension and Director of the Quentin Burdick Center for Cooperatives.  Dr. Olson conducts educational programs and research in evaluating crop marketing strategies, crop outlook and price analysis, and the economics of crop contracting.  As Director of the Center for Cooperatives, he teaches a senior level course on cooperative business management and coordinates the Center’s research and outreach activities. Dr. Olson received his PhD from the University of Missouri in Agricultural Economics, and his M.S. and B.S. in Agricultural Economics from North Dakota State University."},
                 "Tim Petry": {"Website":"https://www.ndsu.edu/agecon/faculty/petry/#c625018",
                                 "Areas of Specialization": "Livestock Marketing Economist",
                                 "Bio":"Tim Petry was raised on a livestock ranch in Northwestern North Dakota. He graduated from North Dakota State University with a major in Agricultural Economics in 1969 and served two years in the US Army. Petry returned to NDSU and completed a Master’s Degree in Agricultural Economics with an agricultural marketing emphasis in1973. He was a member of the teaching/research staff in the Department of Agricultural Economics for 30 years. During his teaching tenure, he taught many marketing courses including several livestock marketing classes, and a very popular introduction to agricultural marketing class. In 2002, Petry retired from teaching and joined the NDSU Extension Service as a Livestock Marketing Economist. He travels extensively in North Dakota and the surrounding area conducting meetings on livestock marketing educational topics. Petry writes a popular monthly “Market Advisor” column on current livestock marketing issues. Copies of his presentations, columns, and other current information affecting the livestock industry are available on his web site: www.ag.ndsu.edu/livestockeconomics. Tim Petry and his wife Shirley have three grown daughters."},
                 "Xudong Rao": {"Website":"https://www.ndsu.edu/agecon/faculty/rao/#c629066",
                                 "Areas of Specialization": "Farm and Agribusiness Management, Risk Analysis, Efficiency and Productivity, Technology Adoption, Food and Agricultural Policy, International Agricultural Development",
                                 "Bio":"Assistant Professor, Department of Agribusiness and Applied Economics, North Dakota State University, 2019  and also served as an a ssistant Professor, Business Economics Group, Wageningen University, The Netherlands, 2015-2019 (Permanent contract granted in 2018)"},
                 "Veeshan Rayamajhee": {"Website":"https://www.ndsu.edu/centers/pcpe/about/directory/veeshan_rayamajhee/",
                                 "Areas of Specialization": "Public Choice and New Institutional Economics",
                                 "Bio":"Veeshan Rayamajhee is a scholar at the Challey Institute for Global Innovation and Growth with the Center for the Study of Public Choice and Private Enterprise and an assistant professor of economics in the Department of Agribusiness and Applied Economics at North Dakota State University. His research combines insights from Public Choice and New Institutional Economics to understand individual and collective responses to covariate shocks. He uses a range of empirical tools to study issues related to disasters, climate adaptation, food and energy security, and environmental externalities. His research has appeared in peer-reviewed journals such as Journal of Institutional Economics, Disasters, Economics of Disasters and Climate Change, Journal of International Development, Food Security, and Renewable Energy. For updates on his research, please visit: veeshan.rayamajhee.com/research. Veeshan teaches courses in macroeconomics and new institutional economics."},
                 "David Ripplinger": {"Website":"https://www.ndsu.edu/agecon/faculty/ripplinger/#c629078",
                                 "Areas of Specialization": "Transportation and Logistics",
                                 "Bio":"David Ripplinger is an Associate Professor in the Department of Agribusiness and Applied Economics at North Dakota State University and bioproducts/bioenergy economics specialist with NDSU Extension. In these roles, David conducts research and provides support to farmers and the bioenergy industry. "},
                 "David Roberts": {"Website":"https://www.ndsu.edu/agecon/faculty/roberts/#c629137",
                                 "Areas of Specialization": "impacts of agricultural production methods on the environment and natural resources",
                                 "Bio":"David Roberts is an Assistant Professor of Agribusiness and Applied Economics at North Dakota State University. His research focuses on the impacts of agricultural production methods on the environment and natural resources. David is particularly interested in the economics of precision agriculture technologies and the response of cropping patterns and land use change to emerging biofuels policy at the Federal level. His doctoral dissertation research investigated the relative profitability of several different mid-season optimal nitrogen rate prediction systems for winter wheat in Oklahoma, and investigated how incorporation of uncertainty in estimated and predicted production functions can increase the profitability of the prediction systems. David’s MS thesis investigated the suitability of water quality trading as a policy instrument for dealing with nutrient runoff from agricultural operations in Tennessee. Results showed conditions in polluted watersheds in Tennessee likely will not support robust trading in water quality allowances or offsets."},
                 "Anupa Sharma": {"Website":"https://www.ndsu.edu/agecon/faculty/sharma/#c629150",
                                 "Areas of Specialization": "International Trade Agreements, Trade Patterns, Distance and Missing Globalization, International Trade and Development",
                                 "Bio":"Anupa Sharma is an Assistant Professor in the Department of Agribusiness and Applied Economics at North Dakota State University. She also serves as the Assistant Director for the Center for Agricultural Policy and Trade Studies (CAPTS). She develops quantitative methods to address issues pertinent to International Trade."},
                 "Cheryl Wachenheim": {"Website":"https://www.ndsu.edu/agecon/faculty/wachenheim/#c629162",
                                 "Areas of Specialization": "agricultural sales, agricultural finance, agricultural marketing, and strategic marketing and management",
                                 "Bio":"Cheryl Wachenheim is a Professor in the Department of Agribusiness and Applied Economics at North Dakota State University. She holds an undergraduate degree in animal sciences from the University of Minnesota, and a Master’s and doctorate in Agricultural Economics and an MBA from Michigan State University. She began her academic career at Illinois State University in Central Illinois and has been on the faculty at NDSU since 1998.  She regularly teaches classes in economics, agricultural sales, agricultural finance, agricultural marketing, and strategic marketing and management.  Research interests focus on eliciting perceptions and valuations from consumers, firms, students and other stakeholders and decision makers.  Analysis then allows for identification of high-value marketing and management strategies.  Cheryl has been a member of the MN Army National Guard since 1998. She is currently the Commander of the 204th Area Medical Support Company in Cottage Grove, Minnesota"},
                 "William Wilson": {"Website":"https://www.ndsu.edu/agecon/faculty/wilson/#c629178",
                                 "Areas of Specialization": "agtechnology development and commercialization, procurement, transportation and logistics, international marketing and competition",
                                 "Bio":"Dr. William W. Wilson received his PhD in Agricultural Economics from the University of Manitoba in 1980. Since then he has been a Professor at North Dakota State University in Agribusiness and Applied Economics with periodic sabbaticals at Stanford University. Recently, he was named as a University Distinguished Professor at NDSU which an honorary position is, and a great achievement.  And, in 2016 he was named the CHS Chair in Risk Management and Trading at NDSU which is an endowed position. In 2017 he was awarded the AAEA 2016 Distinguished Teaching Award (Chicago July 2017). His focus is risk and strategy as applied to agriculture and agribusiness with a particular focus on agtechnology development and commercialization, procurement, transportation and logistics, international marketing and competition. He teaches classes in Commodity Trading, Risk and AgriBusiness Strategy and has taught his Risk Class at Purdue University; and is a visiting scholar at Melbourne University where he visits 2 times/year and advises PhD students in risk and agbiotechnology. Finally, he has now created the NDSU Commodity Trading Room which is a state of art facility for teaching and research in commodity marketing, logistics and trading. He routinely has projects and/or overseas clients and travels internationally 1 week per month.  He led a project for the United States on privatization of the grain marketing system in Russia in the early 1990’s. He currently has projects and/or clients in US, Russia, Ukraine, Mexico, Argentina and Australia. He regularly advises a number of large Agribusiness firms, several major railroads, and several major food and beverage companies and/or governments in other countries. He served as a Board member of the Minneapolis Grain Exchange for 12 years, on the FGIS Advisory Board, and currently serves as a Board member of several regional firms in agtechnology and venture capital (AMITY, BUSHEL), in addition to NCH Capital (New York City which is one of the largest investors in world agriculture). He regularly consults with major agribusiness firms on topics related to above and has worked extensively in the following industries: agtechnology,  logistics, procurement strategy, railroads, barges, ocean shipping, elevators (shuttle development), and processed products (malting and beer, durum and pasta, wheat and bread). He was recognized as one of the top 10 Agricultural Economists in 1995 and more recently as one of the top 1% of agricultural economists by RePEc (Research Papers in Economics). Finally, he has students who are in senior positions in a number of the large agribusinesses including commodity companies, railroads and food and beverage companies."},
                }
faculty_dict


# In[28]:


faculty_df = pd.DataFrame(faculty_dict).T


# In[30]:


faculty_df.loc["Jeremy Jackson"] ["Bio"]


# In[31]:


faculty_df.keys()


# In[32]:


index = faculty_df.index
for ix in index:
    print(ix)
    for key in faculty_df.keys():
        print(key, faculty_df.loc[ix][key])


# In[33]:


faculty_df.keys()


# In[34]:


index = faculty_df.index
for ix in index:
    print(ix)
    for key in faculty_df.keys():
        print(key, faculty_df.loc[ix][key])


# In[35]:


faculty_df[faculty_df["Areas of Specialization"].str.contains("Risk")]


# In[ ]:


lst = ["a", "b", "c"]
"a" in lst


# In[36]:


names = ["Jeremy Jackson", "Raymond March", "Veeshan Rayamajhee"]
faculty_df[faculty_df.index.isin(names)]


# In[37]:


names = faculty_df.index
for name in names:
    print(name)


# In[38]:


faculty_df[faculty_df["Areas of Specialization"].str.contains("resource")]


# In[ ]:




