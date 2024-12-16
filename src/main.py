import os

os.system("python data_preprocessing.py")
os.system("python eda_analysis.py")
os.system("python pca_analysis.py")
#os.system("python cluster_analysis.py")

print("Workflow completed! Check the 'output/' folder for results.")
