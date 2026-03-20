using System;
using System.Collections.Generic;
using System.Text;

namespace MongoDB_C_
{
    public class Book
    {
        public string title;
        public string author;
        public int publishingYear;

        public Book(string title, string author, int publishingYear)
        {
            this.title = title;
            this.author = author;
            this.publishingYear = publishingYear;
        }
    }
}
