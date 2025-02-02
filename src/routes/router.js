/**
 * @file Defines routes for application.
 * @module routes/router
 * @author Miranda Holmlund
 * @version 1.0
 */


import express from 'express'
import { ClusterController } from '../controllers/controller.js'

export const router = express.Router()
const controller = new ClusterController()

router.get('/', (req, res, next) => {
  controller.showFrontPage(req, res)
})

router.post('/data', (req,res,next) => {
  controller.getData(req, res)
})