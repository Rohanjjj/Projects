// summarizer.js

/**
 * Simple Extractive Summarization using Sentence Scoring
 * This is a basic implementation and can be enhanced for better accuracy.
 */

function summarize(text, maxSentences = 5) {
    // Split text into sentences
    const sentences = text.match(/[^\.!\?]+[\.!\?]+/g);
    if (!sentences) return "No content to summarize.";
  
    // Create a frequency table for words
    const wordFrequency = {};
    const stopWords = new Set([
      'the', 'is', 'in', 'and', 'to', 'of', 'a', 'with', 'that', 'for', 'as',
      'on', 'it', 'this', 'at', 'by', 'an', 'be', 'from', 'or', 'are', 'was',
      'but', 'not', 'have', 'has', 'had', 'they', 'their', 'which', 'you',
      'one', 'we', 'can', 'all', 'your', 'more', 'about', 'will', 'if', 'do',
      'so', 'no', 'when', 'what', 'up', 'out', 'there', 'been', 'who', 'get',
      'just', 'some', 'could', 'them', 'like', 'than', 'then', 'now', 'how',
      'into', 'its', 'only', 'also', 'other', 'over', 'did', 'many'
    ]);
  
    const words = text.toLowerCase().match(/\w+/g);
    if (!words) return "No content to summarize.";
  
    words.forEach(word => {
      if (!stopWords.has(word)) {
        wordFrequency[word] = (wordFrequency[word] || 0) + 1;
      }
    });
  
    // Score sentences based on word frequency
    const sentenceScores = sentences.map(sentence => {
      const sentenceWords = sentence.toLowerCase().match(/\w+/g);
      let score = 0;
      if (sentenceWords) {
        sentenceWords.forEach(word => {
          if (wordFrequency[word]) {
            score += wordFrequency[word];
          }
        });
      }
      return { sentence, score };
    });
  
    // Sort sentences by score in descending order
    sentenceScores.sort((a, b) => b.score - a.score);
  
    // Select top N sentences
    const summarySentences = sentenceScores.slice(0, maxSentences).map(s => s.sentence.trim());
  
    // Sort summary sentences in their original order
    summarySentences.sort((a, b) => text.indexOf(a) - text.indexOf(b));
  
    return summarySentences.join(' ');
  }
  