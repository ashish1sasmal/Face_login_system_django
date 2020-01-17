 navigator.getUserMedia = ( navigator.getUserMedia ||
                    navigator.webkitGetUserMedia ||
                    navigator.mozGetUserMedia ||
                    navigator.msGetUserMedia);

var video;
var webcamStream;
if (navigator.getUserMedia) {
  navigator.getUserMedia (

     // constraints
     {
        video: true,
        audio: false
     },

     // successCallback
     function(localMediaStream) {
         video = document.querySelector('video');
        video.srcObject = localMediaStream;
        webcamStream = localMediaStream;
     },

     // errorCallback
     function(err) {
        console.log("The following error occured: " + err);
     }
  );
} else {
  console.log("getUserMedia not supported");
}



var canvas, ctx;

function init() {
// Get the canvas and obtain a context for
// drawing in it
mcanvas = document.getElementById("myCanvas");
ctx = mcanvas.getContext('2d');
}

function login() {
// Draws current image from the video element into the canvas
ctx.drawImage(video,0,0,mcanvas.width,mcanvas.height);
var dataURL = mcanvas.toDataURL('image/png');
document.getElementById("current_image").value=dataURL;

}
