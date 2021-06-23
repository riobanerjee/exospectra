from astroquery.mast import Observations

obs_table = Observations.query_object("M8",radius=".02 deg")
data_products_by_obs = Observations.get_product_list(obs_table[0:2])
print(data_products_by_obs)