def FormString(FILE_NAME):
    query_str=""
    with open(os.path.abspath(FILE_NAME),'r') as csvfile:

    return query_str


def closeDBConnection(con,logger_g):
    con.close()
    


def getDBConnection():

    Conection = psycopg2.connect("host='"+DBhost+"'"+
                                        " port='"+DBport+"'"+
                                        " dbname='"+DBName+"'"+
                                        " user='"+DBUser+"'"+
                                        " password='"+DBPassword+"'")
    return Conection


def loadData(qyeryString,logger_g,doCommit = 'False'):
    logger_g.info(qyeryString)
    con=None
    try:
        con = getDBConnection()
        cur = con.cursor()
        cur.execute(qyeryString)
        if doCommit == 'True':
            con.commit()
            logger.info("Data Inserted ")
    except psycopg2.DatabaseError, e:
        logger.error(traceback.format_exc())
        if con:
            con.rollback()
    finally:
        if con:
            closeDBConnection(con,logger_g)
            
            
            
            
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='../conf/config.ini')
    args = parser.parse_args()
    config = ConfigParser.ConfigParser()
    config.read(args.config)
    DBhost=config.get('DATABASE','DB_HOST')
    DBport=config.get('DATABASE','DB_PORT')
    DBName=config.get('DATABASE','DB_NAME')
    DBUser=config.get('DATABASE','DB_USER')
    DBPassword=config.get('DATABASE','DB_PASSWORD')
    
    
    
