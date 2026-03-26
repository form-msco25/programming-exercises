// src/app.js
import express from "express";
import cors from "cors";
import indexRoutes from "./routes/index.routes.js";
import recommendRoutes from "./routes/recommend.routes.js";
import authRoutes from "./routes/auth.routes.js";


const app = express();

app.use(cors());        // aqui ativa o CORS
app.use(express.json());

//app.get("/", (req, res) => {
  //res.send("Gastrologic API a funcionar");
//});

app.use("/", indexRoutes);
app.use("/recommend", recommendRoutes);
app.use("/auth", authRoutes);


export default app;