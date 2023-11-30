from functions.centroids import Centroid
from functions.blog_data import blog_data, word_stats
from functions.pearson import pearson
import random
import copy

def k_means(data, k, max_iterations) :
  num_of_words = 706
  centroids = []
  for _ in range(k):
    c = Centroid()
    for j in range(num_of_words):
      c.set_word_count(j, random.randint(word_stats[j]['min'], word_stats[j]['max']))
    centroids.append(c)
  for _ in range(max_iterations):
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
    for centroid in centroids:
      for i in range(num_of_words):
        avg = 0
        if centroid.assigned:
          for blog in centroid.assigned:
            avg += blog.counts[i]
            avg /= len(centroid.assigned)
            centroid.set_word_count(i, avg)
    #if old_centroids == centroids : return
  return centroids

data = k_means(blog_data, 5, 10)

k_means = []

for centroid in data:
  blognames = []
  for blog in centroid.assigned:
    blognames.append(blog.blog_name)
  k_means.append(blognames)







