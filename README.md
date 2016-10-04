# WSP
WorkSafe Proxy is simple image proxy that uses the [Yahoo's open_nsfw classification model](https://github.com/yahoo/open_nsfw) to determine if an image is safe or not.

## How does it work?
- You pass an image URI to the application: `http://localhost:5000/http://your-domain.com/test_image.jpg`
- The WSP application will score the image on a scale of 0 to 1. A score of 0 is completely safe for work, and 1 is not safe.
- If the image scored less that 0.1, the app will return the requested image to the client.
- If the image scored greater than 0.1, the application will return a more appropriate image to the client instead of the original request. 

## Docker Quickstart

[Install docker](https://docs.docker.com/engine/installation)

Build the image
```
git clone https://github.com/neufeldtech/wsp.git
cd wsp
docker build . -t wsp
```

Run the image
```
docker run -it -p 5000:5000 wsp
```

Test it out

Visit [http://localhost:5000](http://localhost:5000) in your browser to view the index page and instructions.

To proxy an image, append the image URI to the end of the host URL:

[http://localhost:5000/https://pixabay.com/static/uploads/photo/2016/09/07/23/10/cat-1652880_960_720.jpg](http://localhost:5000/https://pixabay.com/static/uploads/photo/2016/09/07/23/10/cat-1652880_960_720.jpg)
 
If the image is scored **not safe for work**, your source image will be replaced. If your image scored as **safe for work**, you will see your original image.

## Credit

This project makes use following:

- [Yahoo open_nsfw image classification model](https://github.com/yahoo/open_nsfw)