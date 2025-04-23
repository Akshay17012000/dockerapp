const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const BACKEND_URL = 'http://python-backend:4000';

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
    const now = new Date();
    const dayOfWeek = now.toLocaleDateString('en-US', { weekday: 'long' });
    const currentTime = now.toTimeString().split(' ')[0];

    res.render('index', { day_of_week: dayOfWeek, current_time: currentTime });
});

app.post('/submit', async (req, res) => {
    try {
        
        await axios.post(`${BACKEND_URL}/submit`, req.body);
    } catch (err) {
        console.error('Error posting to backend:', err.message);
    }
    res.render('success');
});

app.listen(8000, () => {
    console.log('Server running on http://localhost:8000');
});

