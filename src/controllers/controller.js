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

  /**
   * Gets front page of application.
   * @param {object} req Express request object.
   * @param {object} res Express response object.
   */
  showFrontPage(req, res) {
    try {
      const data = this.data
      res.render('home', { data })
    } catch (error) {
      console.error(error)
    }
  }

  /**
   * Fetches data from k-means service.
   * @param {object} req Express request object.
   * @param {object} res Express response object.
   */
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