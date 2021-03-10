import random
import matplotlib.pyplot as plt


class Kmeans:
    def __init__(self,points,numClusters):
        self.points = points
        self.numClusters = numClusters
        self.clusters = []
    
    #Function that computes distance from one point to another.
    def dist(self,point,centroid):
        d=0
        for i in range(len(centroid)):
            d += (point[i] - centroid[i])**2
        return d

    # Function that evaluates the found clusters with sum of TDSquared of clusters
    def tds(self):
        
        print("Cluster Evaluation:")
        ttsum = 0
        tsum = 0
        count = 1
        for cluster in self.clusters:
            for point in cluster.points:
                tsum += self.dist(point,cluster.centroid)
            print(f"------ Cluster #{count} -------")
            print(f"Centroid: {cluster.centroid}")
            print(f"Points: {cluster.points}")
            print(f"TDS: {tsum}")
            ttsum +=tsum
            tsum = 0
            count += 1
        print("")
        print(f"Solution total TDSquare: {ttsum}")
        
    #A function that runs the Kmeans algorithm
    def run(self):
        
        #You can hardcode a starting point for centroids
        #This also determins number of clusters
        #centroids = [[1.5 , 4],[6.67 , 4],[6.67 , 8.33]]
        
        #Or you can randomly select starting centroids.
        centroids = []
        indicesPicked = []
        while len(centroids) < self.numClusters:
            i = random.randint(0,len(self.points)-1)
            if i not in indicesPicked:
                centroids.append(self.points[i])
        
        thesameCentroids = []
        run = 1
        while centroids != thesameCentroids:
            
            self.clusters = []
            
            for centroid in centroids:
                self.clusters.append(Cluster(centroid))
            
            for point in self.points:
                nearestCluster = self.clusters[0]
                nearestDist = self.dist(point,nearestCluster.centroid)
            
                for cluster in self.clusters:
                    distance = self.dist(point,cluster.centroid)
                    if distance < nearestDist:
                        nearestCluster = cluster
                        nearestDist = distance
                nearestCluster.points.append(point)  

            print(f"------- Run {run} ----------")
            for cluster in self.clusters:
                print(f"Centroid: {cluster.centroid}")
                print(f"Points: {cluster.points}")
                print("")
            run += 1
            thesameCentroids = centroids
            centroids = self.getNewCentroids()

    def getNewCentroids(self):
        newcentroids = []
        for cluster in self.clusters:
            cluster.updateCentroid()
            newcentroids.append(cluster.centroid)
        return newcentroids

class Cluster:
    def __init__(self,centroid):
        self.centroid = centroid
        self.points = []
        
    
    def updateCentroid(self):
        if len(self.points)>0:
            dims = len(self.points[0])
            dimSum = []
            
            for dim in range(dims):
                sum = 0
                for point in self.points:
                    sum += point[dim]
                dimSum.append(sum/len(self.points))
            self.centroid = dimSum





points = [[1,5],[2,3],[3,4],[7,7],[10,1],[6,8],[7,8],[7,9]]

kmeans = Kmeans(points,4)
kmeans.run()
kmeans.tds()