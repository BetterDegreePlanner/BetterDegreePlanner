const express = require('express')
const Class = require('../models/courseModel')
const router = express.Router()


router.get('/list', (req, res) => {
    res.json({mssg: 'GET /list'})
})

router.get('/professor/list', (req, res) => {
    res.json({mssg: 'GET /professor/list'})
})

router.post('/addCourse', (req, res) => {
    res.json({mssg: 'POST /addCourse'})
})

router.get('/:id', (req, res) => {
    res.json({mssg: 'GET /:id'})
})

module.exports = router