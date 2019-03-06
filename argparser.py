    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='../conf/config.ini')
    parser.add_argument('--infile', type=argparse.FileType('r'),
                        required=True)
    parser.add_argument('-log', default='../conf/log')
    args = parser.parse_args()
    config = ConfigParser.ConfigParser()
    config.read(args.config)
    PASSED_INFILE=str(args.infile).split("'")[1]
    LOG_FILE=str(args.log)
