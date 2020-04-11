from GUIx import window
from Image_Recog import detect_faces
from Image_Recog import capture_new_user
from Image_Recog import faces_training
import pickle
import os

path_to_users = os.path.dirname(os.path.abspath(__file__))
path_to_users = os.path.join(path_to_users,'users')

users_det = {}
def loadusrs():
    global users_det
    with open(str(path_to_users + '/users.pickle'),"rb") as fr:
        users_det = pickle.load(fr)
loadusrs()
auth, newusr, usrname = window.isAuth()
success = False
captured = False
hasPermission = False
if auth:
    usrname = usrname.lower()
    print('auth,{}'.format(usrname))
    detect_faces.setup()
    # detect_faces.detect()
    success = detect_faces.authenticate(usrname)
    if success:
        print('Login Successfull')
    else:
        print('Login Failed')
    # success=detect_faces.detect(usrname)
elif newusr:
    capture_new_user.setup(usrname)
    captured = capture_new_user.capture_photos()
    print('scanned')
    faces_training.trainusrs()
    print('Trained')
    loadusrs()
else:
    print('no')

hasPermission = (auth & success) | (newusr & captured)
print(hasPermission)

if not hasPermission:
    if auth:
        window.show_failed_status('Login')
    else:
        window.show_failed_status('Sign Up')
    exit(0)

#now user has permission
if auth:
    window.show_success_status('Login')
else:
    window.show_success_status('Sign Up')
window.show_sites(usrname,users_det[usrname])