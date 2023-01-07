from urlextract import URLExtract
ext=URLExtract()
def fetch_stats(selected_user,df):
    if selected_user!='Overall':
        df=df[df['user']==selected_user.replace('\n',' ')]
    #number of total messages
    num_messages=df.shape[0]
    #number of total words
    words=[]
    for i in df['message']:
        words.extend(i.split())
    #number of media
    num_media=df[df['message']=='<Media omitted>\n'].shape[0]
    #number of links
    links=[]
    for i in df['message']:
        links.extend(ext.find_urls(i))
        
    return num_messages,len(words),num_media,len(links)