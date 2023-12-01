from functions.centroids import Centroid
from functions.blog_data import blog_data, word_stats
from functions.pearson import pearson
import random

#Creates an array of Centroids with clusters
def k_means(data, k) :
  num_of_words = 706
  centroids = []
  for _ in range(k):
    c = Centroid()
    for j in range(num_of_words):
      c.set_word_count(j, random.randint(word_stats[j]['min'], word_stats[j]['max']))
    centroids.append(c)
    old_centroids = None
  while True:
    best_centroids = []
    [centroid.clearAssigned() for centroid in centroids]
    for blog in data:
      distance = float('inf')
      best = Centroid()
      for centroid in centroids:
        cDistance = pearson(centroid, blog)
        if(cDistance < distance) :
          best = centroid
          distance = cDistance
      best.assign(blog)
      best_centroids.append(best)
    if best_centroids == old_centroids : break
    old_centroids = best_centroids
    for centroid in centroids:
      for i in range(num_of_words):
        avg = 0
        if centroid.assigned:
          for blog in centroid.assigned:
            avg += blog.counts[i]
            avg /= len(centroid.assigned)
            centroid.set_word_count(i, avg)
  return centroids

#Manages the centroids into sendable data for json format.
def get_k_means_data() :
  data = k_means(blog_data, 5)
  k_data = []
  for centroid in data:
    blognames = []
    for blog in centroid.assigned:
      blognames.append(blog.blog_name)
    k_data.append(blognames)
  return k_data







