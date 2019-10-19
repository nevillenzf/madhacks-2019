const routes = require('express').Router();
const Pool = require('pg').Pool
const pool = new Pool({
    user: 'me',
    host: 'localhost',
    database: 'metricdata',
    password: 'password',
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