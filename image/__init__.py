import cv2
import os

class ImagePreprocessor(object):
    """Image preprocessor. Have methods to read image from path and flow directory.
    
    """
    def __init__(self):
        pass
    def read_image(self,path,shape=None):
        """Reads image with given path. If shape is given the output image will be 
        numpy ndarray of that shape. Otherwise the shape of output image will not be changed.
        
        Arguments:
            path {string} -- Absolute or relative path to image
        
        Keyword Arguments:
            shape {tuple} -- Shape of output image (default: {None})
        Returns:
            numpy.ndarray -- Image with given path.
        """
        assert os.path.exists(path), "Path '"+str(path)+"' does not exist"
        assert shape is None or len(shape)==2 or len(shape)==3,"Shape value should be none or list of len 2 or len 3"
        image = cv2.imread(path)
        if not(shape is None) and  (len(shape)==2 or shape[2]==1):
            image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        if not (shape is None):
            image = cv2.resize(image,(shape[0],shape[1]))
        if not(shape is None):
            image = image.reshape(shape)
        return image
    def __get_all_image_files(self,path,ext=[".jpg",".png",".bmp"]):
        """Gets all image files which have extension given by `ext` argument.
        
        Arguments:
            path {str} -- Path to folder containing images
        
        Keyword Arguments:
            ext {list} -- Extesion of images (default: {[".jpg",".png",".bmp"]})
        
        Returns:
            list -- list containg file names of all images inside directory given by `path` argument
        """
        assert os.path.exists(path), "Path '"+str(path)+"' does not exist"
        assert type(str) or len(ext) == 0,"ext should contain at list one element"
        if type(ext)==str:
            ext = [ext]
        output = []
        for file_name in os.listdir(path):
            _,e = os.path.splitext(file_name)
            if e in ext:
                output+=[file_name]
        return output
    def read_all_images(self,directory,image_shape,ext =[".jpg",".png",".bmp"]):
        """Reads all images given inside directory.
        
        Arguments:
            directory {str} -- Path to directory
            image_shape {tuple} -- output images shape
        
        Keyword Arguments:
            ext {list} -- Extension of images to read (default: {[".jpg",".png",".bmp"]})
        
        Returns:
            numpy.ndarray -- Numpy array for images inside directory
        """

        assert os.path.exists(path), "Path '"+str(directory)+"' does not exist"
        assert type(str) or len(ext) == 0,"ext should contain at list one element"
        assert len(image_shape)==2 or len(image_shape)==3,"Image Shape should be list of len 2 or len 3"
        
        image_files = self.__get_all_image_files(directory,ext)
        if len(image_shape) == 3:
            output = np.zeros((len(image_files),image_shape[0],image_shape[1],image_shape[2]))
        else:
            output = np.zeros((len(image_files),image_shape[0],image_shape[1]))
        for i in range(len(image_files)):
            image = self.read_image(os.path.join(directory,image_files[i]),image_shape)
            output[i] = image
        return output
    
        
        
    
    
    