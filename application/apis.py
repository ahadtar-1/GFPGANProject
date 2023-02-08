"""
The module comprises of the different APIs
"""

from flask import Flask, request, send_file, render_template
import os
from operations import upsampling_image, face_enhancement

app = Flask(__name__, template_folder='template')


@app.route("/")
def selection_menu()-> None:
    """
    The api functions that display the selection menu

    Parameters
    ----------
    None

    Returns
    -------
    None

    """

    return render_template("page.html")


@app.route('/upsampleimg', methods = ['GET', 'POST'])
def upsample_img()-> str:
    """
    The api function that generates an upsampled image from an image

    Parameters
    ----------
    None
    
    Returns
    -------
    str
    
    """

    if request.method == 'POST':
        f = request.files['file']
        fileName = f.filename
        f.save(os.path.join("",fileName))
        path = upsampling_image(os.path.join("",fileName))
        if path:
            return send_file(path)
        else:
            return "No image"


@app.route('/enhanceimg', methods = ['GET', 'POST'])
def enhance_img()-> str:
    """
    The api function that generates an enhanced image from a noisy image
    
    Parameters
    ----------
    None
    
    Returns
    -------
    str
    
    """

    if request.method == 'POST':
        f = request.files['file']
        fileName = f.filename
        f.save(os.path.join("",fileName))
        path = face_enhancement(os.path.join("",fileName))
        if path:
            return send_file(path)
        else:
            return "No image"
            