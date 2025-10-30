import click, requests

API = "https://yesay-backend.fly.dev/api"

@click.group()
def main(): pass

@main.command()
@click.argument("token")
@click.option("--display", "-d", required=True)
@click.argument("files", nargs=-1)
def upload(token, display, files):
    fd = {"display_name": display, "token": token}
    fl = [("files", open(f, "rb")) for f in files]
    r = requests.post(f"{API}/upload", data=fd, files=fl)
    print(r.json())

if __name__ == "__main__":
    main()
