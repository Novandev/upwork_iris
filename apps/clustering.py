from sklearn.cluster import AgglomerativeClustering

from apps.data import df
city_codes = {"SF":0, "NYC":1, "ATL":2}
state_codes ={"CA":1, "NY":2, "GA":3}
hospital_names = ["Hospital 1", "Hospital 2", "Hospital 3"]
df_dropped = df[df['Date'] == '06/01/2020']
df_dropped = df_dropped.drop(["Hospital Name","Date"], axis=1)
df_dropped['City'] = df_dropped['City'].map(city_codes)
df_dropped['State'] = df_dropped['State'].map(state_codes)

clustering_labels = AgglomerativeClustering().fit_predict(df_dropped)


df_dropped['Hospital Cluster'] = clustering_labels
df_dropped['Hospital Name'] = hospital_names
df_clusters = df_dropped

