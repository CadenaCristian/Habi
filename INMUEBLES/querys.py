originalQuery = """select pr.address, pr.city, pr.price, pr.description, st.name from property as pr 
inner join status_history as sth on sth.property_id = pr.id
inner join status as st on sth.status_id = st.id"""
allData = " where st.id in (3,4,5)"
filter_by_year = " and pr.year = '{}'"
filter_year_city = filter_by_year+" and pr.city = '{}'"
filter_year_city_state = " where pr.year = '{}'" + \
    filter_year_city + " and st.id = {}"
