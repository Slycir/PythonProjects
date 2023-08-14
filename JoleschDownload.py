import requests
import os

def main():

    # Navigate to save location (OneDrive/Desktop/Python/JoleschPhotos)
    home = os.path.expanduser("~")
    if os.path.isdir(f"{home}\\OneDrive\\Desktop") == True:
        desktop = f"{home}\\OneDrive\\Desktop"
    else:
        desktop = f"{home}\\Desktop"
    if os.path.isdir(f"{desktop}\\Python") == False:
        os.mkdir(f"{desktop}\\Python")
    if os.path.isdir(f"{desktop}\\Python\\JoleschPhotos") == False:
        os.mkdir(f"{desktop}\\Python\\JoleschPhotos")
    os.chdir(f"{desktop}\\Python\\JoleschPhotos")

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'referer': 'https://www.teamphotonetwork.com/QPPlus/Proofs.aspx',
        'accept-Encoding': 'gzip, deflate, br',
        'accept-Language': 'en-US,en;q=0.9',
        "authority": "www.teamphotonetwork.com"
    }

    # Get the camera ID
    cameraID = input("Enter the camera ID: ")

    # Get the photo tag
    photoTag = input("Enter the photo tag: ")

    # Get the photo number range
    photoRange = input("Enter the photo range (ex. 1-10): ")
    photoRange = photoRange.split("-")
    photoRange = list(range(int(photoRange[0]),int(photoRange[1])+1))
    photoRange = [str(i) for i in photoRange]

    # Numbers at least 4 digits long
    for i in range(len(photoRange)):
        if len(photoRange[i]) == 1:
            photoRange[i] = "000" + photoRange[i]
        elif len(photoRange[i]) == 2:
            photoRange[i] = "00" + photoRange[i]
        elif len(photoRange[i]) == 3:
            photoRange[i] = "0" + photoRange[i]

    # Set the URL
    urlBase = f"https://www.teamphotonetwork.com/qpplus/handlers/hzp.ashx?o=27201051&r={cameraID}&f={photoTag}"

    # Download the photos
    for i in photoRange:
        print(f"Downloading {photoTag}{i}.jpg...")
        photoRaw = requests.get(urlBase+i,headers=headers)
        photo = photoRaw.content
        open(f"{photoTag}_{i}.jpg","wb").write(photo)

main()