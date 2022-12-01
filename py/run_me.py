"""
1. start db container
2. start pgadmin container
3. run script
 - get query
 - create table
 - insert results
4. run script
 - create datamarts
 - create datamart
"""
#QUERY_LAUNHCHES
#QUERY_LINKS
#QUERY_HISTORIES
#QUERY_MISSIONS
#QUERY_ROCKETS

import custom
import get_space_data
from queries import QUERY_HISTORIES, QUERY_LAUNCHES, QUERY_LINKS, QUERY_MISSIONS, QUERY_ROCKETS
from dm_queries import DM_LAUNCHES, DM_MISSIONS, DM_ROCKETS
url = 'https://api.spacex.land/graphql'
conn_str = 'postgresql://elon:musk@localhost:8001/spacex-db'

#get raw data
launches = get_space_data.get_table(QUERY_LAUNCHES, url)
links = get_space_data.get_table(QUERY_LINKS, url)
histories = get_space_data.get_table(QUERY_HISTORIES, url)
missions = get_space_data.get_table(QUERY_MISSIONS, url)
rockets = get_space_data.get_table(QUERY_ROCKETS, url)


#get raw dataframe
launches_df_raw = get_space_data.make_df(launches, 'launches')
links_df_raw = get_space_data.make_df(links, 'launches')
histories_df_raw = get_space_data.make_df(histories, 'histories')



#get flat dataframe
launches_df = custom.for_launches_df(launches_df_raw)
links_df = custom.for_links_df(links_df_raw)
histories_df = custom.for_histories_df(histories_df_raw)
missions_df = get_space_data.make_df(missions, 'missions')
rockets_df = get_space_data.make_df(rockets, 'rockets')


# KILL None values at launch_success
s = []
z =''
for i in launches_df['launch_success']:
    if i != None:
        s.append(i)
    else:
        s.append(z)
launches_df.drop(columns=['launch_success'], axis = 1, inplace=True)
launches_df['launch_success'] = s

#KILL None values at links
for name, values in links_df.iteritems():
    s = []
    z =''
    for i in links_df[name]:
        if i != None:
            s.append(i)
        else:
            s.append(z)
    links_df.drop(columns=[name], axis = 1, inplace=True)
    links_df[name] = s

#kill null values in histories
for name, values in histories_df.iteritems():
    s = []
    z =''
    for i in histories_df[name]:
        if i != None:
            s.append(i)
        else:
            s.append(z)
    histories_df.drop(columns=[name], axis = 1, inplace=True)
    histories_df[name] = s


#kill % symbols in links
links_df.loc[8]['wiki'] = 'wiki_ok'
links_df.loc[15]['wiki'] = 'wiki_ok'
links_df.loc[85]['wiki'] = 'wiki_ok'
links_df.loc[58]['link'] = 'link_ok'
links_df.loc[58]['wiki'] = 'wiki_ok'

#splitting mission manufacturers
s =[]
for i in missions_df['manufacturers']:
    s.append(', '.join(i))
missions_df.drop(columns=['manufacturers'], axis = 1, inplace=True)
missions_df['manufacturers_l'] = s


#get CREATE TABLE statement
ct_launches = get_space_data.create_tab_query('launches',launches_df)
ct_links = get_space_data.create_tab_query('links',links_df)
ct_histories = get_space_data.create_tab_query('histories', histories_df)
ct_missions = get_space_data.create_tab_query('missions', missions_df)
ct_rockets = get_space_data.create_tab_query('rockets', rockets_df)


#get INSERT INTO statement
ii_launches = get_space_data.insert_into_query_arr('launches', launches_df)
ii_links = get_space_data.insert_into_query_arr('links', links_df)
ii_histories = get_space_data.insert_into_query_arr('histories', histories_df)
ii_missions = get_space_data.insert_into_query_arr('missions', missions_df)
ii_rockets = get_space_data.insert_into_query_arr('rockets', rockets_df)


#create tables
get_space_data.run_query(ct_launches)
get_space_data.run_query(ct_links)
get_space_data.run_query(ct_histories)
get_space_data.run_query(ct_missions)
get_space_data.run_query(ct_rockets)

#load data
for i in ii_launches:
    get_space_data.run_query(i)

for i in ii_links:
    get_space_data.run_query(i)

for i in ii_histories:
    get_space_data.run_query(i)

for i in ii_missions:
    get_space_data.run_query(i)
for i in ii_rockets:
    get_space_data.run_query(i)

get_space_data.run_query(DM_MISSIONS)
get_space_data.run_query(DM_ROCKETS)
get_space_data.run_query(DM_LAUNCHES)
