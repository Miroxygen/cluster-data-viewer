/**
 * @file Defines controller for application.
 * @module controllers/controller
 * @author Miranda Holmlund
 * @version 1.0
 */

import fetch from "node-fetch"


/**
 * Controller for clusterapplication.
 */
export class ClusterController {

  constructor() {
    this.data
  }

  showFrontPage(req, res) {
    const data = this.data
    res.render('home', { data })
  }

  async getData(req, res) {
    try {
      const respone = await fetch("http://localhost:8083/get-kmeans")
      const data = await respone.json()
      this.data = data
      res.redirect('.')
    } catch (error) {
      console.error(error)
    }
  }
}