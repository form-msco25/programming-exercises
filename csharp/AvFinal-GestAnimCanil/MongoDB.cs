using System;
using System.Collections.Generic;
using System.Text;
using MongoDB.Driver;

namespace AvFinal_GestAnimCanil
{
    public class MongoDB
    {
        private readonly string connectionString = "mongodb+srv://formacaomsco_db_user:MDB,2525!@cluster0.mfozkxk.mongodb.net/?appName=Cluster0";
        private readonly string dataBaseName = "MyDataBase";
        private readonly string collectionName = "Animais";

        private MongoClient client;
        private IMongoDatabase database;
        private IMongoCollection<Cao> collection;
        public MongoDB()
        {   
            client = new MongoClient(connectionString);
            database = client.GetDatabase(dataBaseName);
            collection = database.GetCollection<Cao>(collectionName);
        }

        public void Guardar(List<Cao> animais)
        {
            if (animais.Count > 0)
                collection.InsertMany(animais);
        }

        public List<Cao> Ler()
        {
            return collection.Find(_ => true).ToList();
        }
    }
}
