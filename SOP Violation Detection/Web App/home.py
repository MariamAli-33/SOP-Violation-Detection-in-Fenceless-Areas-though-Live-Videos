import streamlit as st
st. set_page_config(layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
from app import *
from menu import Menu

from PIL import Image
import streamlit.components.v1 as components
import streamlit as st
import subprocess
import sys

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 2

def home():
      components.html(
"""
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
  integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
  integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
  integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<style>
  /* Carousel base class */
.carousel {
    margin-bottom: 4rem;
  }

  /* Since positioning the image, we need to help out the caption */
.carousel-caption {
    bottom: 3rem;
    z-index: 10;
  }

  /* Declare heights because of positioning of img element */



.carousel-item {
    height: 35rem;
    background-color: #777;
  }

.carousel-item .video-fluid {
    display: block;
    height: auto;
    max-width: 100%;
    line-height: 1;
    margin: auto;
    width: 100%; // Add this
  }

.carousel-item h1, p {
    color: white;

  }

.carousel-item p a {
    background-color: #2e4c7d;
    border: none;
  }

  /* Second Section----- */
:root {
    --jumbotron-padding-y: 3rem;
  }

.jumbotron {

    margin-bottom: 0;
    background-image: url('https://img.freepik.com/free-vector/people-connecting-jigsaw-pieces-head-together_53876-64617.jpg?t=st=1652898400~exp=1652899000~hmac=cf41034cafc3882dc9ca763b4395834d526991372467562b5ba2b3b03b3f8a35&w=1060');
    height: 500px;
    background-repeat: no-repeat;
    background-size: cover;
    background-size: auto 100%;
  }


.jumbotron-heading {
    font-weight: 300;
  }

.jumbotron .container {
    max-width: 40rem;
    padding: 10px 120px;
    margin: 40px 530px;
  }

footer {
    padding-top: 3rem;
    padding-bottom: 3rem;
  }

footer p {
    margin-bottom: .25rem;
    color:black;
  }

.box-shadow {
    box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .05);
  }

.lead{
  color:black;
}
  /*Card Deck*/
.card-deck {
    border-radius: 5%;
  }

.card-deck .card-body {
    background-color: #ffff;
    color: black;
  }

.card-deck .card-body p {
    color: black;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  }

.card-deck button {
    background-color: #2e4c7d;
    color: white;
  }

#accordion .card-header {
    background-color: #86b59b;
  }

#accordion button {
    color: white;
  }

.jumbotron p a {
    background-color: #2e4c7d;
    color: white;
  }

.card-img-top {
    width: 100%;
    height: 20vw;
    object-fit: cover;
  }
</style>
<main role="main">

  <!--Carousel Wrapper-->
  <div id="video-carousel-example2" class="carousel slide carousel-fade" data-ride="carousel">
    <!--Indicators-->
    <ol class="carousel-indicators">
      <li data-target="#video-carousel-example2" data-slide-to="0" class="active"></li>
      <li data-target="#video-carousel-example2" data-slide-to="1"></li>
      <li data-target="#video-carousel-example2" data-slide-to="2"></li>
    </ol>
    <!--/.Indicators-->
    <!--Slides-->
    <div class="carousel-inner" role="listbox">
      <!-- First slide -->
      <div class="carousel-item active">
        <!--Mask color-->
        <div class="view">
          <!--Video source-->
          <video class="video-fluid" autoplay loop muted>
            <source
              src="https://assets.mixkit.co/videos/preview/mixkit-virtual-neural-network-in-motion-3d-30276-large.mp4"
              type="video/mp4" />
          </video>
          <div class="mask rgba-indigo-light"></div>
        </div>
        <!--Caption-->
        <div class="carousel-caption" style="float:right; padding: 10px 20px; right: 60px">
          <div class="animated fadeInDown">
            <div class="container">
              <div class="carousel-caption  text-right">
                <h1>Intellegent System</h1>
                <h4>Based on Computer Vision and Deep Learning techniques</h4>
              </div>
            </div>
          </div>
        </div>
        <!--Caption-->
      </div>
      <!-- /.First slide -->

      <!-- Second slide -->
      <div class="carousel-item">
        <!--Mask color-->
        <div class="view">
          <!--Video source-->
          <video class="video-fluid" autoplay loop muted>
            <source
              src="https://assets.mixkit.co/videos/preview/mixkit-coronavirus-inside-the-human-body-26741-large.mp4"
              type="video/mp4" />
          </video>
          <div class="mask rgba-purple-slight"></div>
        </div>

        <!--Caption-->
        <div class="carousel-caption">
          <div class="animated fadeInDown">
            <div class="container">
              <div class="carousel-caption">
                <h1>SOPs Voilation Detection</h1>
                <h4>To prevent the spread of contagious disease by<br>ensruring Face Masking and Social Distancing</h4>
              </div>
            </div>
          </div>
        </div>
        <!--Caption-->
      </div>
      <!-- /.Second slide -->

      <!-- Third slide -->
      <div class="carousel-item ">
        <!--Mask color-->
        <div class="view">
          <!--Video source-->
          <video class="video-fluid" autoplay loop muted>
            <source
              src="https://assets.mixkit.co/videos/preview/mixkit-touring-a-symbolic-digital-world-of-artificial-intelligence-and-information-12765-large.mp4"
              type="video/mp4" />
          </video>
          <div class="mask rgba-black-strong"></div>
        </div>

        <!--Caption-->
        <div class="carousel-caption">
          <div class="animated fadeInDown">
            <div class="container">
              <div class="carousel-caption text-left">
                <h1>Low Resolution Footage</h1>
                <h4>Provides efficient results in less-favorable environment</h4>
              </div>
            </div>
          </div>
        </div>
        <!--Caption-->
      </div>
      <!-- /.Third slide -->
    </div>
    <!--/.Slides-->
    <!--Controls-->
    <a class="carousel-control-prev" href="#video-carousel-example2" role="button" data-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#video-carousel-example2" role="button" data-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
    <!--/.Controls-->
  </div>
  <!--Carousel Wrapper-->

  <!-- Features -->
  <div class="pricing-header px-3 py-3 pt-md-2 pb-md-4 mx-auto text-center  ">
    <h2 class="h1">SYSTEM FEATURES</h2>
    <p class="lead">Features are the functionalities that Detexive provides to complete a set of tasks or actions and
      produce desired outcome</p>
  </div>
  <div class="album py-5 bg-light">
    <div class="container">
      <div class="card-deck">
        <!-- Card -->
        <div class="card">
          <!-- Card image -->
          <div class="view overlay">
            <img class="card-img-top"
              src="https://img.freepik.com/free-vector/vector-illustration-medical-staff-examine-patient-through-microscope-detection-virus_143808-101.jpg?w=1060"
              alt="Image Detection">
            <a>
              <div class="mask rgba-white-slight"></div>
            </a>
          </div>
          <!-- Card content -->
          <div class="card-body">

            <!-- Title -->
            <h4 class="card-title">Image Detection</h4>
            <hr>
            <!-- Text -->
            <p class="card-text">Image processing for the detection of the face mask and social distancing shall take
              image input from the user and return processed output. </p>
            <button class="btn btn-rounded btn-md">Read more</button>
          </div>
        </div>
        <!-- Card -->
        <!-- Card -->
        <div class="card">
          <!-- Card image -->
          <div class="view overlay">
            <img class="card-img-top"
              src="https://img.freepik.com/free-vector/content-creator-editing-video-footage-studio-editor-publishing-viral-video-social-media-multimedia-production-flat-vector-illustration-motion-design-concept-banner-landing-web-page_74855-21752.jpg?t=st=1652894398~exp=1652894998~hmac=70cd4642b30f91f610609eff8900da8163fd8cf28a7fabbf4a812aaf93b22a55&w=996"
              alt="Card image cap">
            <a>
              <div class="mask rgba-white-slight"></div>
            </a>
          </div>
          <!-- Card content -->
          <div class="card-body">

            <!-- Title -->
            <h4 class="card-title">Video Detection</h4>
            <hr>
            <!-- Text -->
            <p class="card-text">Video Footage can be provided from the current directory of the user and feed into
              either of modules for the deteciton of violations. </p>
            <button class="btn btn-rounded btn-md">Read more</button>
          </div>
        </div>
        <!-- Card -->
        <!-- Card -->
        <div class="card">
          <!-- Card image -->
          <div class="view overlay">
            <img class="card-img-top"
              src="https://img.freepik.com/free-vector/people-standing-queue-bank-withdrawing-cash-money-flat-vector-illustration-ai-face-recognition-with-camera-access-digital-safety-analysis-control-concept_74855-13202.jpg?t=st=1652894166~exp=1652894766~hmac=1dfcf2bef0da7037c18bc330e61f5231b5ac4b3d310478a0b19c0edc2f047975&w=1380"
              alt="Card image cap">
            <a>
              <div class="mask rgba-white-slight"></div>
            </a>
          </div>
          <!-- Card content -->
          <div class="card-body">

            <!-- Title -->
            <h4 class="card-title">Live Stream Detection </h4>
            <hr>
            <!-- Text -->
            <p class="card-text">Through CCTV camera or even the mobile camera can be used for the live detection of
              either of SOP (face mask/social distancing)</p>
            <button class="btn btn-rounded btn-md">Read more</button>
          </div>
        </div>
        <!-- Card -->
      </div>
      <!---FAQs--->
      <div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
        <h2 class="h1">FAQs</h2>
        <p class="lead">Here are answers to all your users' regular queries in one place for them to access at an
          instant.</p>
      </div>
      <div id="accordion">
        <div class="card">
          <div class="card-header" id="headingOne">
            <h5 class="mb-0">
              <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true"
                aria-controls="collapseOne">
                Which technologies are used for detection purposes?
              </button>
            </h5>
          </div>

          <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
            <div class="card-body">
              Detectixe has used the technologies of Yolo and OpenCV. YOLOv3 (You Only Look Once, Version 3) is a
              real-time object detection algorithm that identifies specific objects in videos, live feeds, or images.
              Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and
              supports CPU and GPU computation. •YOLO: Real-Time Object Detection. •ImageNet Classification
            </div>
          </div>
        </div>
        <div class="card">
          <div class="card-header" id="headingTwo">
            <h5 class="mb-0">
              <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo"
                aria-expanded="false" aria-controls="collapseTwo">
                Can we detect both violations in a single video/image?
              </button>
            </h5>
          </div>
          <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
            <div class="card-body">
              Yes, Detectixe allows you to detect face mask and social distancing detection within a video or image
              footage. Just go to SOPs Detection (Both) > Choose Video or Image Detection from dashboard > Upload your
              file and now you are ready to go!
            </div>
          </div>
        </div>
        <div class="card">
          <div class="card-header" id="headingThree">
            <h5 class="mb-0">
              <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseThree"
                aria-expanded="false" aria-controls="collapseThree">
                Can the system detect violation through live footage?
              </button>
            </h5>
          </div>
          <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
            <div class="card-body">
              Yes, Detectixe allows you to detect face mask and social distancing detection within a video or image
              footage. Just go to dashboard and click on live detection and turn on the camera for the live detection of
              violation.
            </div>
          </div>
        </div>
      </div>
      <!---FAQs End--->
      <!---Team Start--->
      <section class="jumbotron text-right">
        <div class="container">
          <h1 class="jumbotron-heading">Meet our Developement Team</h1>
          <p class="lead text-muted">Group Member 01: Mariam Ali <br> Email Address: <br>mali.bese18seecs@seecs.edu.pk <br> Group Member 02: Ayesha Siddiqua <br> Email Address: asiddiqua.bese18seecs@seecs.edu.pk </p>
        </div>
      </section>
      <!---Team End--->
      <!-- FOOTER -->
      <footer class="container text-center">
        <p>&copy; 2022 Detexive Company, Inc. &middot; <a>Privacy</a> &middot; <a>Terms and Conditions </a></p>
      </footer>
      """,
      height=2400,
      )
def services():
      components.html("""
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
      <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous">
      </script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous">
      </script>
      <div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
        <h1 class="h1">SERVICES</h1>
        <p class="lead">Detexive offers you services free on trail basis. Each service ensures accurate and efficient results.
          as follows</p>
      </div>

      <div class="container">
        <div class="card-deck mb-3 text-center">
          <div class="card mb-4 box-shadow">
            <div class="card-header bg-info">
              <h4 class="my-0 font-weight-normal ">Face Mask Detection</h4>
            </div>
            <div class="card-body">
              <ul class="list-unstyled mt-3 mb-4">
                <li>Categorisation of Masked and Non-masked Faces</li>
                <li>Image And Video Files Supported (PNG, JPEG, MP4, AVI, etc.) </li>
                <li>Support Mobile Camera and CCTV Camera Feed</li>
                <li>Interactive User Interface (Dashboard)</li>
              </ul>
              <button type="button" class="btn btn-lg btn-block btn-info">Learn More</button>
            </div>
          </div>
          <div class="card mb-4 box-shadow">
            <div class="card-header bg-secondary">
              <h4 class="my-0 font-weight-normal">Social Distancing Detection</h4>
            </div>
            <div class="card-body">
              <ul class="list-unstyled mt-3 mb-4">
                <li>Detection of Social Distancing; 6 feet distance</li>
                <li>Image And Video Files Supported (PNG, JPEG, MP4, AVI, etc.) </li>
                <li>Support Mobile Camera and CCTV Camera Feed</li>
                <li>Interactive User Interface (Dashboard)</li>
              </ul>
              <button type="button" class="btn btn-lg btn-block btn-secondary">Learn More</button>
            </div>
          </div>
          <div class="card mb-4 box-shadow">
            <div class="card-header bg-warning">
              <h4 class="my-0 font-weight-normal">SOP Detection (Both)</h4>
            </div>
            <div class="card-body">
              <ul class="list-unstyled mt-3 mb-4">
                <li>Get Face Mask and Social Distancing Detection in one</li>
                <li>Image And Video Files Supported (PNG, JPEG, MP4, AVI, etc.) </li>
                <li>Support Mobile Camera and CCTV Camera Feed</li>
                <li>Interactive User Interface (Dashboard)</li>
              </ul>
              <button type="button" class="btn btn-lg btn-block btn-warning">Learn More</button>
            </div>
          </div>
        </div>
        <!-- FOOTER -->
        <footer class="container text-center">
          <p>&copy; 2022 Detexive Company, Inc. &middot; <a>Privacy</a> &middot; <a>Terms and Conditions </a></p>
        </footer>
        """,height=650,)

def research():
      components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
          integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
          integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous">
        </script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
          integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous">
        </script>
        <style>

        </style>
        <main role="main" class="container">
          <div class="my-3 p-3 bg-white rounded box-shadow">
            <h4 class="border-bottom border-gray pb-2 mb-0">Recent News</h4>
            <div class="media text-muted pt-3">
              <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                <strong class="d-block text-gray-dark">A new state of the art for unsupervised computer vision</strong>
                Scientists at MIT's CSAIL developed an algorithm to handle one of the most difficult challenges in
                computer vision: assigning labels to every pixel in the world without human intervention.
              </p>
            </div>
            <div class="media text-muted pt-3 bg-light">
              <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                <strong class="d-block text-gray-dark">Dan Huttenlocher ponders our human future in an age of artificial
                  intelligence</strong>
                Bringing disciplines together, according to the dean of the MIT Schwarzman College of Computing, is the
                greatest way to meet the challenges and opportunities provided by rapid advances in computing.
              </p>
            </div>
            <div class="media text-muted pt-3  bg-light">
              <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                <strong class="d-block text-gray-dark">Security tool guarantees privacy in surveillance footage</strong>
                Without learning personal information about people, "Privid" might let officials collect secure public
                health statistics or enable transportation departments to track pedestrian density and movement.
              </p>
            </div>
            <div class="col-md-12 mt-2 text-right">
              <button type="button" class="btn btn-secondary">Learn More</button>
            </div>
          </div>

          <div class="my-3 p-3 bg-white rounded box-shadow">
            <h4 class="border-bottom border-gray pb-2 mb-0">GitHub Suggestions</h4>
            <div class="media text-muted pt-3">
              <img data-src="holder.js/32x32?theme=thumb&bg=007bff&fg=007bff&size=1" alt="" class="mr-2 rounded">
              <div class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                <div class="d-flex justify-content-between align-items-center w-100">
                  <strong class="text-gray-dark">Darknet YOLO</strong>
                  <a href="https://github.com/pjreddie/darknet">Follow</a>
                </div>
                <span class="d-block">https://github.com/pjreddie/darknet</span>
              </div>
            </div>
            <div class="media text-muted pt-3">
              <img data-src="holder.js/32x32?theme=thumb&bg=007bff&fg=007bff&size=1" alt="" class="mr-2 rounded">
              <div class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                <div class="d-flex justify-content-between align-items-center w-100">
                  <strong class="text-gray-dark">OpenCV Python Platform</strong>
                  <a href="https://github.com/opencv/opencv">Follow</a>
                </div>
                <span class="d-block">https://github.com/opencv/opencv</span>
              </div>
            </div>
            <div class="media text-muted pt-3">
              <img data-src="holder.js/32x32?theme=thumb&bg=007bff&fg=007bff&size=1" alt="" class="mr-2 rounded">
              <div class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                <div class="d-flex justify-content-between align-items-center w-100">
                  <strong class="text-gray-dark">Compputer Vision Receipies</strong>
                  <a href="https://github.com/microsoft/computervision-recipes">Follow</a>
                </div>
                <span class="d-block">https://github.com/microsoft/computervision-recipes</span>
              </div>
            </div>
            <!-- FOOTER -->
            <footer class="container text-center mt-5">
              <p>&copy; 2022 Detexive Company, Inc. &middot; <a>Privacy</a> &middot; <a>Terms and Conditions </a></p>
            </footer>
            """,
            height=800,
            )
def tools():
      components.html("""
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
              integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
              crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
              integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
              crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
              integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
              crossorigin="anonymous"></script>
            <div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
              <p class="h1">TOOLS USED</p>
              <p class="lead">Detexive supports following tools and technologies</p>
            </div>
            <hr>
            <div class="row m-2">
              <div class="col-4">
                <div class="list-group" id="list-tab" role="tablist">
                  <a class="list-group-item list-group-item-action active" id="list-home-list" data-toggle="list"
                    href="#list-home" role="tab" aria-controls="home">OpenCV</a>
                  <a class="list-group-item list-group-item-action" id="list-profile-list" data-toggle="list"
                    href="#list-profile" role="tab" aria-controls="profile">YoloV3 and v4</a>
                  <a class="list-group-item list-group-item-action" id="list-messages-list" data-toggle="list"
                    href="#list-messages" role="tab" aria-controls="messages">Anaconda</a>
                  <a class="list-group-item list-group-item-action" id="list-settings-list" data-toggle="list"
                    href="#list-settings" role="tab" aria-controls="settings">Darknet(NN Framework)</a>
                </div>
              </div>
              <div class="col-8">
                <div class="tab-content" id="nav-tabContent">
                  <div class="tab-pane fade show active" id="list-home" role="tabpanel"
                    aria-labelledby="list-home-list">For Image classification, object localization and object
                    recognition
                    OpenCV is a programming library that focuses on real-time computer vision.
                    It was created by Intel and then sponsored by Willow Garage and Itseez.
                    The Apache 2 licence makes the library cross-platform and free to use.
                  </div>
                  <div class="tab-pane fade" id="list-profile" role="tabpanel" aria-labelledby="list-profile-list">You
                    Only Look Once, Version 3 (YOLOv3) is a real-time object detection system that recognises specific
                    things in films, live feeds, and photos.
                    To detect an item, YOLO uses features learned by a deep convolutional neural network.
                    Joseph Redmon and Ali Farhadi produced the first three versions of YOLO. </div>
                  <div class="tab-pane fade" id="list-messages" role="tabpanel" aria-labelledby="list-messages-list">
                    Anaconda is a Python and R programming language distribution for scientific computing that promises
                    to make package management and deployment easier.
                    Data-science packages for Windows, Linux, and macOS are included in the release. </div>
                  <div class="tab-pane fade" id="list-settings" role="tabpanel" aria-labelledby="list-settings-list">
                    Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to
                    install, and supports CPU and GPU computation. •YOLO: Real-Time Object Detection.</div>
                </div>
              </div>
            </div>
            <!-- FOOTER -->
            <footer class="container mt-5 text-center">
              <p>&copy; 2022 Detexive Company, Inc. &middot; <a>Privacy</a> &middot; <a>Terms and Conditions </a></p>
            </footer>
            """, height=580,)
def contact():
      components.html("""
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
              integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
              crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
              integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
              crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
              integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
              crossorigin="anonymous"></script>
            <div class="jumbotron">
              <h2 class="h2">Background</h2>
              <p class="lead">Learn more about Detexive</p>
              <hr class="my-4">
              <p>The system will cover the detection of two major SOP violations; Not wearing of face mask in a public
                area, Not standing 6 feet/2 meters apart. The priority is the collection of raw footage of CCTV Cameras/
                Surveillance cameras from various public places such as hospitals, pharmacy shops, small shops, and
                marts. These raw footages will surely be the input for the database creation module. The datasets will
                be generated through the “Dataset Creation Module”, to which we shall feed the footages and train the
                predictive detection models. Next to the database creation module, is the detection subsystem that will
                be a composite of two modules for corresponding SOPs; 1) Face Mask Detection Module, 2) Person Detection
                Module. All the violations detected each of module demands Update/Warning Subsystem, in which two
                processes will be completed in parallel i.e., updating the violators’ information and generation of
                alert notification and prompt it on the application.</p>
              <p class="lead">
                <a class="btn btn-info btn-lg text-white" role="button">Learn more</a>
              </p>
            </div>
            <p class="h4">Find Us on Google Map</p>
            <div id="map-container-google-1" class="z-depth-1-half map-container" style="height: 500px">
  <iframe src="https://www.google.com/maps/embed?pb=!1m26!1m12!1m3!1d13286.664047785549!2d72.97633183393957!3d33.63990089152022!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m11!3e6!4m3!3m2!1d33.6361413!2d72.9789334!4m5!1s0x38df9675aaaaaaab%3A0xc5180922c44eb86b!2snust%20on%20google%20maps!3m2!1d33.642488799999995!2d72.99300099999999!5e0!3m2!1sen!2s!4v1652921113411!5m2!1sen!2s" width="1280" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
            <!-- FOOTER -->
            <footer class="container mt-5 text-center">
              <p>&copy; 2022 Detexive Company, Inc. &middot; <a>Privacy</a> &middot; <a>Terms and Conditions </a></p>
            </footer>
            """, height=1200, )


           
             


            # """)
            # if st.button('Say hello'):
            # app.run()
            # else:
            # st.text("")
x = Menu()
EXAMPLE_NO=2
            # def run_once(f):
            # def wrapper(*args, **kwargs):
            # if not wrapper.has_run:
            # wrapper.has_run = True
            # return f(*args, **kwargs)
            # wrapper.has_run = False
            # return wrapper

selected = x.streamlit_menu(EXAMPLE_NO)
if selected == "Services":
      services()
if selected == "News":
      research()
if selected == "Tools":
      tools()
if selected == "Contact":
      contact()
if selected == "Detect":
      app.run()
if selected == "Home":
  home()