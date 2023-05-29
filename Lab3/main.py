import os
from pathlib import Path
import csv

def countFiles():
    fileName = input("Введите путь к папке: ")
    file = Path(fileName)
    files = os.listdir(file)
    print(f"В данной папке содержатся следующие объекты: {files}\nИх количество: {len(files)}")



def get_posts(posts_history):
    print("post number;nickname;post text;number of likes")
    with open("Post.csv", "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(*row)
            posts_history[row[0]] = row[1:]


def sort_posts_number(posts_history):
    print("\nОтсортируем по количеству лайков: ")
    for elem in sorted(posts_history.items(), key = lambda para: int(para[1][2])):
        print(elem[0], *elem[1])


def sort_posts_str(posts_history):
    print("\nОтсортируем по тексту поста: ")
    for elem in sorted(posts_history.items(), key = lambda para: para[1][1]):
        print(elem[0], *elem[1])
    print("")


def output_by_criterion(posts_history):
    criterion = input("Введите количсество лайков: \n")
    print(f'\nСтроки, в которых количество лайков больше "{criterion}": ')
    for elem in posts_history:
        if posts_history[elem][2] >= criterion:
            print(elem, *posts_history[elem])


def write_to_csv(posts_history):
    newKey = input("Введите номер поста: ")
    new_nickname = input("Введите никнейм пользователя который создал пост: ")
    newtextpost = input("Введите текст поста: ")
    new_number_of_likes = input("Введите количество лайков поста: ")
    posts_history[newKey] = [new_nickname, newtextpost, new_number_of_likes]
    with open('Post.csv', 'w', encoding='utf-8') as f:
        for elem in posts_history:
            f.write(elem + ',' + posts_history[elem][0] + ',' + posts_history[elem][1] + ',' + posts_history[elem][2] + '\n')


def main():
    countFiles()
    posts_history = {}
    get_posts(posts_history)
    sort_posts_number(posts_history)
    sort_posts_str(posts_history)
    output_by_criterion(posts_history)
    write_to_csv(posts_history)


if __name__ == "__main__":
    main()