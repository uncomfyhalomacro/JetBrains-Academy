# Write your code here
from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False', echo=False)

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='NULL')
    deadline = Column(Date, default=datetime.today().date())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

id_add = 0
while True:
    print("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit""")
    u_input = input()
    if u_input == '0':
        break
    elif u_input == '6':
        print("\nChose the number of the task you want to delete:")
        to_delete = session.query(Table).order_by(Table.deadline).all()
        if to_delete:
            for n, task in enumerate(to_delete):
                print("{}. {}".format(n + 1, task))
            chosen = int(input())
            session.delete(to_delete[chosen - 1])
            session.commit()
            print("The task has been deleted!\n")
        else:
            print("Nothing to delete\n")
    elif u_input == '5':
        print()

        new_row = Table(task=input("Enter task\n"),
                        deadline=datetime.strptime(input("Enter deadline:\n"), "%Y-%m-%d").date())
        session.add(new_row)
        session.commit()
        print('The task has been added!\n')
    elif u_input == '4':
        print("\nMissed tasks:")
        today = datetime.today().date()
        missed = session.query(Table).filter(Table.deadline < today).order_by(Table.deadline).all()
        if not missed:
            print("Nothing is missed!\n")

        else:
            le = len(missed)
            d = datetime.today().date()
            z = 0
            dictionary = {}
            while le > 0:
                z += 1
                d = datetime.today().date() - timedelta(days=z)
                date_row = session.query(Table).order_by(Table.deadline).filter(Table.deadline == d).all()
                if date_row != []:
                    le -= 1

            for t in range(z + 1, 0, -1):
                d = datetime.today().date() - timedelta(days=t)
                date_row = session.query(Table).filter(Table.deadline == d).all()
                if date_row != []:
                    for item in date_row:
                        dictionary[item] = d
            nz = 0
            for task, date in dictionary.items():
                nz += 1
                print("{}. {}. {}".format(nz, task, date.strftime("%d %b")), )
        print()
    elif u_input == '3':
        rows = session.query(Table).order_by(Table.deadline).all()
        print("\nALL tasks:")
        for n, task in enumerate(rows):
            print("{}. {}".format(n + 1, task))
        print()

    elif u_input == '2':
        print()
        for n in range(0, 7):
            day = datetime.today().date() + timedelta(days=n)
            date_row = session.query(Table).filter(Table.deadline == day).all()
            if date_row == []:
                print(day.strftime("%A %d %b") + ':')
                print("Nothing to do!\n")
            else:
                print(day.strftime("%A %d %b") + ':')
                for n, task in enumerate(date_row):
                    print("{}. {}".format(n + 1, task))
                print()

    elif u_input == '1':
        print()
        today = datetime.today().date()
        date_row = session.query(Table).filter(Table.deadline == today).all()
        if date_row == []:
            print(datetime.today().date().strftime("%A %d %b") + ':')
            print("Nothing to do!\n")
        else:
            print("\nToday", datetime.today().date().strftime("%A %d %b") + ':')
            for n, task in enumerate(date_row):
                print("{}. {}".format(n + 1, task))
            print()
