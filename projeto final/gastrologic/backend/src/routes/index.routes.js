// src/routes/index.routes.js
import { Router } from "express";
const router = Router();

router.get("/health", (req, res) => {
  res.json({ ok: true, service: "backend", sprint: 1 });
});

export default router;