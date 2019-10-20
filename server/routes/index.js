const dotenv = require('dotenv');
dotenv.config();
const routes = require('express').Router();
const Pool = require('pg').Pool
const pool = new Pool({
    user: process.env.DBUSER || "me",
    host: process.env.DBHOST || "localhost",
    database: process.env.DBNAME || "metricdata",
    password: process.env.DBPASS || "password",
    port: 5432,
});

// Want to serve files here!
routes.get('/', (req, res) => {
    res.status(200).json({ message: 'Connected!' });
});

routes.get('/companies/', (req, res) =>{
    pool.query('SELECT * FROM metric_data ORDER BY calc_score DESC', (error, results) => {
        if (error) throw error;
        res.status(200).json(results.rows);
    });
});

module.exports = routes;