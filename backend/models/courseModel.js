const mongoose = require('mongoose')

const Schema = mongoose.Schema
//defines the structure of the data
const courseSchema = new Schema({
    title:{
        type: String,
        required: true
    },
    courseDep: {
        type: String,
        required: true
    },
    courseNum: {
        type: Number,
        required: true
    },
    professors: {
        type: Array,
        required: true
    },
    preReqs: {
        type: Array,
        required: false
    },
    concurrentEnrollment: {
        type: Array,
        required: false
    }
}, {timestamps:true})

module.exports = mongoose.model('Course', courseSchema)