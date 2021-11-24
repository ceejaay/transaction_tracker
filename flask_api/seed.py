from sqlalchemy import create_engine
DATABASE_URI = 'postgresql+psycopg2://cjem:password@hostname/homework_dev'
engine = create_engine(DATABASE_URI)


