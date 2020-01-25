import numpy

class SVD():

    def descomponer(self, vector: list, full_matrices=True, compute_uv=True):
        #Preparación de los datos
        npVector = numpy.array(vector)
        columnas = len(npVector)

        try:
            vfilas = len(npVector[0])
        except TypeError:
            vfilas = 'A'

        filas = vfilas if vfilas!='A' else -1
        reshapedVector = npVector.reshape(columnas,filas)

        #variables a recordar para reconstrucción
        self.forma = reshapedVector.shape
        self.full = full_matrices

        #Generación de las matrices reducidas
        if compute_uv:
            u, s, vh = numpy.linalg.svd(reshapedVector,full_matrices,compute_uv)
            return u, s, vh
        else:
            s = numpy.linalg.svd(reshapedVector,full_matrices,compute_uv)
            return s 

    def reconstruir(self, u: list, s: list, vh: list):
        #reconstrucción
        columnas, filas = self.forma

        if self.full:
            smat = numpy.zeros(self.forma)
            dimension = len(s)
            smat[:dimension, :dimension] =  numpy.diag(s)
        else:
            smat =  numpy.diag(s)
        
        recons = numpy.dot(u,numpy.dot(smat,vh))

        if filas == 1:
            recons = recons.reshape(1,-1)

        #recons = recons.tolist()
        return recons

    def obtenerFormaOriginal(self):
        return self.forma