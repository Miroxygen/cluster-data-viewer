import math

#Pearson for blogwordcount
def pearson(centroid, blog) :
  sumC = 0; sumB = 0; sumCsq = 0; sumBsq = 0; pSum = 0
  no_of_words = 706
  for i in range(no_of_words):
    word_count_c = centroid.word_count[i]['count']
    word_count_b = blog.counts[i]
    sumC += word_count_c
    sumB += word_count_b
    sumCsq = word_count_c ** 2
    sumBsq = word_count_b ** 2
    pSum = word_count_c * word_count_b
  num = pSum - (sumC * sumB / no_of_words)
  den = math.sqrt((sumCsq - sumC ** 2 / no_of_words) * (sumBsq - sumB ** 2 / no_of_words))
  return 1.0 - num / den

