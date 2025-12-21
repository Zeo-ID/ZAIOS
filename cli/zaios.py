import argparse
from users import add_user, disable_user, list_users

def main():
    parser = argparse.ArgumentParser(prog="zaios")
    sub = parser.add_subparsers(dest="command")

    user = sub.add_parser("user")
    user_sub = user.add_subparsers(dest="action")

    add = user_sub.add_parser("add")
    add.add_argument("username")
    add.add_argument("--email", required=True)
    add.add_argument("--role", required=True)

    disable = user_sub.add_parser("disable")
    disable.add_argument("username")

    user_sub.add_parser("list")

    args = parser.parse_args()

    if args.command == "user":
        if args.action == "add":
            add_user(args.username, args.email, args.role)
        elif args.action == "disable":
            disable_user(args.username)
        elif args.action == "list":
            list_users()

if __name__ == "__main__":
    main()
