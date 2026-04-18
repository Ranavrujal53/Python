# Simple Base Version of PostBoard

import datetime

# In-memory storage
users = {"admin": "admin"}  # sample user
posts = []

# Login function
def login():
    print("Login to PostBoard")
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        return username
    else:
        print("Invalid credentials")
        return None

# Create a post
def create_post(author):
    title = input("Enter post title: ")
    desc = input("Enter post description: ")
    date = datetime.date.today()
    posts.append({"author": author, "title": title, "description": desc, "date": str(date)})
    print("Post created successfully!")

# View all posts
def view_posts():
    if not posts:
        print("No posts yet!")
        return
    for post in posts:
        print("\n--- Post ---")
        print(f"Author: {post['author']}")
        print(f"Title : {post['title']}")
        print(f"Date  : {post['date']}")
        print(f"Desc  : {post['description']}")

# Main program
def main():
    user = login()
    if not user:
        return
    while True:
        print("\n1. Create Post\n2. View Posts\n3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            create_post(user)
        elif choice == "2":
            view_posts()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()