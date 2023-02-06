import urllib.request as urllib

while True:
    def main(url):
        print("checking conectivity")

        response = urllib.urlopen(url)
        print("connected to", url, "successfully")
        print("the response code was: ", response.getcode())

    print("Do you want to check if a sit is up? ")
    print("")
    input_url = input("enter site you want to check: ")

main(input_url)
