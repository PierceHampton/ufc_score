import kagglehub

# Download latest version
path = kagglehub.dataset_download("jerzyszocik/ufc-fight-forecast-complete-gold-modeling-dataset")

print("Path to dataset files:", path)
