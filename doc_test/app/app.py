from utils.utils import not_base_class
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def disp_sad_robot():
    """ I really should not be called on import """
    img = mpimg.imread('index.jpeg')
    imgplot = plt.imshow(img)
    plt.show()

def main():
    """ main loop"""
    disp_sad_robot()

main()

if __name__ == '__main__':
    main()
