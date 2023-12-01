
#Creates blogdata with retriavable namespaces blog_name and counts
class BlogData:
    def __init__(self, blog_name, counts):
        self.blog_name = blog_name
        self.counts = counts

def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file]
    data = []
    for line in lines[1:]:
        values = line.strip().split('\t')
        blog_name = values[0]
        counts = [int(value) for value in values[1:]]
        blog_data = BlogData(blog_name, counts)
        data.append(blog_data)
    return data

blog_data = readfile("src\python\\functions\\blogdata.txt")

#Creates an array with min-max values for word, making it hardcoded but
#saving time when running k_means
word_stats = {}
for data in blog_data:
    counts = data.counts
    for word_index, count in enumerate(counts):
        word_name = word_index
        if word_name not in word_stats:
            word_stats[word_name] = {'min': count, 'max': count}
        else:
            word_stats[word_name]['min'] = min(word_stats[word_name]['min'], count)
            word_stats[word_name]['max'] = max(word_stats[word_name]['max'], count)


