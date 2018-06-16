
  state = {
    weight : [],
    books : [
      'Judges',
      'Micah',
      'Proverbs',
      'Revelation',
      'Deuteronomy',
      'Haggai',
      '3 John',
      '1 Kings',
      'Mark',
      'Matthew',
      '1 Thessalonians',
      'Daniel',
      'Malachi',
      'Colossians',
      'Ruth',
      'Genesis',
      '2 Samuel',
      'Obadiah',
      'Esther',
      'Exodus',
      'Jeremiah',
      'Ephesians',
      'Habakkuk',
      'Luke',
      'Song of Solomon',
      'Jonah',
      'Acts',
      'Job',
      'Titus',
      '2 Timothy',
      'James',
      '2 John',
      'Isaiah',
      '2 Thessalonians',
      '1 Chronicles',
      '1 Timothy',
      'Leviticus',
      '1 Peter',
      'Psalms',
      'Zephaniah',
      'Joel',
      'Nahum',
      'Jude',
      '2 Chronicles',
      'Hosea',
      'Zechariah',
      'Nehemiah',
      'John',
      '1 John',
      'Lamentations',
      'Amos',
      '1 Samuel',
      'Joshua',
      '1 Corinthians',
      'Ezra',
      'Romans',
      '2 Corinthians',
      'Hebrews',
      'Ezekiel',
      '2 Peter',
      'Philippians',
      'Numbers',
      'Philemon',
      'Galatians',
      '2 Kings',
      'Ecclesiastes']
  }

  clickHandler = () => {
    this.getBookWeight();
  }

  getCharCount = (str) => {
    return str.split('').length;
  }

  getBookWeight = () => {
    const {books,weight} = this.state;
    const word = ESV;
    let charCount = 0;

    books.forEach( book => {
      const bookContent =  word[book];
      const bookChapterCount = Object.keys(bookContent).length;

      for (const chapter in bookContent) {
        // Lists all the verses in an array given a chapter
        const versesInChapter = bookContent[chapter];
        for (const verse in versesInChapter) {
          charCount += this.getCharCount(versesInChapter[verse]);
        }

      }

      const oldWeight = this.state.weight;
      oldWeight.push({ [`${book}`] : charCount})
      // reset
      this.setState({weight : oldWeight})
      this.state.weight
      charCount = 0;
    })
  }