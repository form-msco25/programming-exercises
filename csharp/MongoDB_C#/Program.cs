using MongoDB.Driver;

namespace MongoDB_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string connectionString = "mongodb+srv://formacaomsco_db_user:MDB,2525!@cluster0.mfozkxk.mongodb.net/?appName=Cluster0";
            string dataBaseName = "MyDataBase";
            string collectionName = "book";

            var client = new MongoClient(connectionString);
            var database = client.GetDatabase(dataBaseName); // quando não existem dados na db, esta linha insere dados
            var collection = database.GetCollection<Book>(collectionName);

            Book book1 = new Book("Crônica de uma Morte Anunciada", "Gabriel García Márquez", 1981);
            collection.InsertOne(book1);
        }
    }
}
