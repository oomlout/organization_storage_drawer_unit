$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										hull() {
											translate(v = [-51.85, 31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [51.85, 31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [-51.85, -31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [51.85, -31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
										}
									}
									union() {
										translate(v = [0.0, -8.25, -0.1]) {
											hull() {
												translate(v = [-42.75, 5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [42.75, 5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [-42.75, -5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [42.75, -5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
											}
										}
										translate(v = [0.0, 0.0, -0.1]) {
											hull() {
												translate(v = [-37.25, 13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [37.25, 13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [-37.25, -13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [37.25, -13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
											}
										}
										translate(v = [-49.25, -29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [-49.25, 29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [49.25, -29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [49.25, 29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [-47.25, 3.15, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, 3.15, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [-47.25, -23.85, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, -23.85, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
									}
								}
							}
						}
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-28.0, -16.05, 0]) {
											cube(size = [15.0, 7.8, 6.0]);
										}
									}
									union() {
										translate(v = [-28.1, -16.05, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 15.2) {
													polygon(points = [[1.6999999999999997, -0.1], [7.8999999999999995, -0.1], [7.8999999999999995, 6.1]]);
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [13.0, -16.05, 0]) {
											cube(size = [15.0, 7.8, 6.0]);
										}
									}
									union() {
										translate(v = [12.9, -16.05, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 15.2) {
													polygon(points = [[1.6999999999999997, -0.1], [7.8999999999999995, -0.1], [7.8999999999999995, 6.1]]);
												}
											}
										}
									}
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 209.0]) {
			rotate(a = [0, 180, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										hull() {
											translate(v = [-51.85, 31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [51.85, 31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [-51.85, -31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [51.85, -31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
										}
									}
									union() {
										translate(v = [0.0, -8.25, -0.1]) {
											hull() {
												translate(v = [-42.75, 5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [42.75, 5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [-42.75, -5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [42.75, -5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
											}
										}
										translate(v = [0.0, 0.0, -0.1]) {
											hull() {
												translate(v = [-37.25, 13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [37.25, 13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [-37.25, -13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [37.25, -13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
											}
										}
										translate(v = [-49.25, -29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [-49.25, 29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [49.25, -29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [49.25, 29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [-47.25, 3.15, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, 3.15, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [-47.25, -23.85, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, -23.85, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
									}
								}
							}
						}
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-28.0, -16.05, 0]) {
											cube(size = [15.0, 7.8, 6.0]);
										}
									}
									union() {
										translate(v = [-28.1, -16.05, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 15.2) {
													polygon(points = [[1.6999999999999997, -0.1], [7.8999999999999995, -0.1], [7.8999999999999995, 6.1]]);
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [13.0, -16.05, 0]) {
											cube(size = [15.0, 7.8, 6.0]);
										}
									}
									union() {
										translate(v = [12.9, -16.05, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 15.2) {
													polygon(points = [[1.6999999999999997, -0.1], [7.8999999999999995, -0.1], [7.8999999999999995, 6.1]]);
												}
											}
										}
									}
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [-44.65, 12.25, 6.0]) {
			rotate(a = [90, 180, 0]) {
				difference() {
					union() {
						translate(v = [-2.5, 0, 0]) {
							rotate(a = [0, 90, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, 2.5]) {
											rotate(a = [0, -90, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		translate(v = [-2.5, -12.0, 0.5]) {
																			cube(size = [8.0, 12.0, 12.0]);
																		}
																		translate(v = [-2.5, -0.05, 4.0]) {
																			cube(size = [5.0, 3.0, 5.0]);
																		}
																	}
																	union() {
																		translate(v = [0, -7.0, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				difference() {
																					union() {
																						translate(v = [-20.0, -3.4619999999999997, 0]) {
																							cube(size = [20, 6.9239999999999995, 3]);
																						}
																						linear_extrude(height = 3) {
																							polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
																						}
																					}
																					union();
																				}
																			}
																		}
																		translate(v = [0, 3.0500000000000003, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				cylinder(h = 22.95, r = 1.8);
																			}
																		}
																	}
																}
															}
														}
														translate(v = [0, -197.0, 13.0]) {
															rotate(a = [180, 0, 0]) {
																difference() {
																	union() {
																		translate(v = [-2.5, -12.0, 0.5]) {
																			cube(size = [8.0, 12.0, 12.0]);
																		}
																		translate(v = [-2.5, -0.05, 4.0]) {
																			cube(size = [5.0, 3.0, 5.0]);
																		}
																	}
																	union() {
																		translate(v = [0, -7.0, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				difference() {
																					union() {
																						translate(v = [-20.0, -3.4619999999999997, 0]) {
																							cube(size = [20, 6.9239999999999995, 3]);
																						}
																						linear_extrude(height = 3) {
																							polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
																						}
																					}
																					union();
																				}
																			}
																		}
																		translate(v = [0, 3.0500000000000003, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				cylinder(h = 22.95, r = 1.8);
																			}
																		}
																	}
																}
															}
														}
														translate(v = [-2.5, -196.8, 11.5]) {
															cube(size = [8.0, 196.6, 3.0]);
														}
														translate(v = [-2.5, -100.0, 14.45]) {
															cube(size = [12.0, 3.0, 6.05]);
														}
													}
													union();
												}
											}
										}
									}
									union();
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [-44.65, 5.75, -2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-0.35, 0, 0]) {
											hull() {
												translate(v = [-4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [-4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
											}
										}
										translate(v = [-2.5, -2.5, 2.35]) {
											cube(size = [5.0, 5.0, 3.0]);
										}
									}
									union() {
										translate(v = [0, 0, 0]) {
											rotate(a = [0, 180, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.8);
														}
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [-1.5, -3.0, 2.4]) {
											cube(size = [3.0, 6.0, 3.0500000000000003]);
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[-2.7, 4.75], [-1.9, 5.55], [-2.7, 5.55]]);
												}
											}
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[2.7, 4.75], [1.9, 5.55], [2.7, 5.55]]);
												}
											}
										}
										translate(v = [-4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [-4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
									}
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [-44.65, 5.75, 211.4]) {
			rotate(a = [180, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-0.35, 0, 0]) {
											hull() {
												translate(v = [-4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [-4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
											}
										}
										translate(v = [-2.5, -2.5, 2.35]) {
											cube(size = [5.0, 5.0, 3.0]);
										}
									}
									union() {
										translate(v = [0, 0, 0]) {
											rotate(a = [0, 180, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.8);
														}
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [-1.5, -3.0, 2.4]) {
											cube(size = [3.0, 6.0, 3.0500000000000003]);
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[-2.7, 4.75], [-1.9, 5.55], [-2.7, 5.55]]);
												}
											}
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[2.7, 4.75], [1.9, 5.55], [2.7, 5.55]]);
												}
											}
										}
										translate(v = [-4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [-4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
									}
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [44.65, 12.25, 6.0]) {
			rotate(a = [90, 180, 0]) {
				difference() {
					union() {
						translate(v = [-2.5, 0, 0]) {
							rotate(a = [0, 90, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, 2.5]) {
											rotate(a = [0, -90, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		translate(v = [-2.5, -12.0, 0.5]) {
																			cube(size = [8.0, 12.0, 12.0]);
																		}
																		translate(v = [-2.5, -0.05, 4.0]) {
																			cube(size = [5.0, 3.0, 5.0]);
																		}
																	}
																	union() {
																		translate(v = [0, -7.0, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				difference() {
																					union() {
																						translate(v = [-20.0, -3.4619999999999997, 0]) {
																							cube(size = [20, 6.9239999999999995, 3]);
																						}
																						linear_extrude(height = 3) {
																							polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
																						}
																					}
																					union();
																				}
																			}
																		}
																		translate(v = [0, 3.0500000000000003, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				cylinder(h = 22.95, r = 1.8);
																			}
																		}
																	}
																}
															}
														}
														translate(v = [0, -197.0, 13.0]) {
															rotate(a = [180, 0, 0]) {
																difference() {
																	union() {
																		translate(v = [-2.5, -12.0, 0.5]) {
																			cube(size = [8.0, 12.0, 12.0]);
																		}
																		translate(v = [-2.5, -0.05, 4.0]) {
																			cube(size = [5.0, 3.0, 5.0]);
																		}
																	}
																	union() {
																		translate(v = [0, -7.0, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				difference() {
																					union() {
																						translate(v = [-20.0, -3.4619999999999997, 0]) {
																							cube(size = [20, 6.9239999999999995, 3]);
																						}
																						linear_extrude(height = 3) {
																							polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
																						}
																					}
																					union();
																				}
																			}
																		}
																		translate(v = [0, 3.0500000000000003, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				cylinder(h = 22.95, r = 1.8);
																			}
																		}
																	}
																}
															}
														}
														translate(v = [-2.5, -196.8, 11.5]) {
															cube(size = [8.0, 196.6, 3.0]);
														}
														translate(v = [-2.5, -100.0, 14.45]) {
															cube(size = [12.0, 3.0, 6.05]);
														}
													}
													union();
												}
											}
										}
									}
									union();
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [44.65, 5.75, -2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-0.35, 0, 0]) {
											hull() {
												translate(v = [-4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [-4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
											}
										}
										translate(v = [-2.5, -2.5, 2.35]) {
											cube(size = [5.0, 5.0, 3.0]);
										}
									}
									union() {
										translate(v = [0, 0, 0]) {
											rotate(a = [0, 180, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.8);
														}
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [-1.5, -3.0, 2.4]) {
											cube(size = [3.0, 6.0, 3.0500000000000003]);
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[-2.7, 4.75], [-1.9, 5.55], [-2.7, 5.55]]);
												}
											}
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[2.7, 4.75], [1.9, 5.55], [2.7, 5.55]]);
												}
											}
										}
										translate(v = [-4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [-4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
									}
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [44.65, 5.75, 211.4]) {
			rotate(a = [180, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-0.35, 0, 0]) {
											hull() {
												translate(v = [-4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [-4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
											}
										}
										translate(v = [-2.5, -2.5, 2.35]) {
											cube(size = [5.0, 5.0, 3.0]);
										}
									}
									union() {
										translate(v = [0, 0, 0]) {
											rotate(a = [0, 180, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.8);
														}
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [-1.5, -3.0, 2.4]) {
											cube(size = [3.0, 6.0, 3.0500000000000003]);
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[-2.7, 4.75], [-1.9, 5.55], [-2.7, 5.55]]);
												}
											}
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[2.7, 4.75], [1.9, 5.55], [2.7, 5.55]]);
												}
											}
										}
										translate(v = [-4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [-4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
									}
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [-44.65, -14.75, 6.0]) {
			rotate(a = [90, 180, 0]) {
				difference() {
					union() {
						translate(v = [-2.5, 0, 0]) {
							rotate(a = [0, 90, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, 2.5]) {
											rotate(a = [0, -90, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		translate(v = [-2.5, -12.0, 0.5]) {
																			cube(size = [8.0, 12.0, 12.0]);
																		}
																		translate(v = [-2.5, -0.05, 4.0]) {
																			cube(size = [5.0, 3.0, 5.0]);
																		}
																	}
																	union() {
																		translate(v = [0, -7.0, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				difference() {
																					union() {
																						translate(v = [-20.0, -3.4619999999999997, 0]) {
																							cube(size = [20, 6.9239999999999995, 3]);
																						}
																						linear_extrude(height = 3) {
																							polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
																						}
																					}
																					union();
																				}
																			}
																		}
																		translate(v = [0, 3.0500000000000003, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				cylinder(h = 22.95, r = 1.8);
																			}
																		}
																	}
																}
															}
														}
														translate(v = [0, -197.0, 13.0]) {
															rotate(a = [180, 0, 0]) {
																difference() {
																	union() {
																		translate(v = [-2.5, -12.0, 0.5]) {
																			cube(size = [8.0, 12.0, 12.0]);
																		}
																		translate(v = [-2.5, -0.05, 4.0]) {
																			cube(size = [5.0, 3.0, 5.0]);
																		}
																	}
																	union() {
																		translate(v = [0, -7.0, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				difference() {
																					union() {
																						translate(v = [-20.0, -3.4619999999999997, 0]) {
																							cube(size = [20, 6.9239999999999995, 3]);
																						}
																						linear_extrude(height = 3) {
																							polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
																						}
																					}
																					union();
																				}
																			}
																		}
																		translate(v = [0, 3.0500000000000003, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				cylinder(h = 22.95, r = 1.8);
																			}
																		}
																	}
																}
															}
														}
														translate(v = [-2.5, -196.8, 11.5]) {
															cube(size = [8.0, 196.6, 3.0]);
														}
														translate(v = [-2.5, -100.0, 14.45]) {
															cube(size = [12.0, 3.0, 6.05]);
														}
													}
													union();
												}
											}
										}
									}
									union();
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [-44.65, -21.25, -2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-0.35, 0, 0]) {
											hull() {
												translate(v = [-4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [-4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
											}
										}
										translate(v = [-2.5, -2.5, 2.35]) {
											cube(size = [5.0, 5.0, 3.0]);
										}
									}
									union() {
										translate(v = [0, 0, 0]) {
											rotate(a = [0, 180, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.8);
														}
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [-1.5, -3.0, 2.4]) {
											cube(size = [3.0, 6.0, 3.0500000000000003]);
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[-2.7, 4.75], [-1.9, 5.55], [-2.7, 5.55]]);
												}
											}
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[2.7, 4.75], [1.9, 5.55], [2.7, 5.55]]);
												}
											}
										}
										translate(v = [-4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [-4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
									}
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [-44.65, -21.25, 211.4]) {
			rotate(a = [180, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-0.35, 0, 0]) {
											hull() {
												translate(v = [-4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [-4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
											}
										}
										translate(v = [-2.5, -2.5, 2.35]) {
											cube(size = [5.0, 5.0, 3.0]);
										}
									}
									union() {
										translate(v = [0, 0, 0]) {
											rotate(a = [0, 180, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.8);
														}
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [-1.5, -3.0, 2.4]) {
											cube(size = [3.0, 6.0, 3.0500000000000003]);
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[-2.7, 4.75], [-1.9, 5.55], [-2.7, 5.55]]);
												}
											}
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[2.7, 4.75], [1.9, 5.55], [2.7, 5.55]]);
												}
											}
										}
										translate(v = [-4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [-4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
									}
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [44.65, -14.75, 6.0]) {
			rotate(a = [90, 180, 0]) {
				difference() {
					union() {
						translate(v = [-2.5, 0, 0]) {
							rotate(a = [0, 90, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, 2.5]) {
											rotate(a = [0, -90, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		translate(v = [-2.5, -12.0, 0.5]) {
																			cube(size = [8.0, 12.0, 12.0]);
																		}
																		translate(v = [-2.5, -0.05, 4.0]) {
																			cube(size = [5.0, 3.0, 5.0]);
																		}
																	}
																	union() {
																		translate(v = [0, -7.0, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				difference() {
																					union() {
																						translate(v = [-20.0, -3.4619999999999997, 0]) {
																							cube(size = [20, 6.9239999999999995, 3]);
																						}
																						linear_extrude(height = 3) {
																							polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
																						}
																					}
																					union();
																				}
																			}
																		}
																		translate(v = [0, 3.0500000000000003, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				cylinder(h = 22.95, r = 1.8);
																			}
																		}
																	}
																}
															}
														}
														translate(v = [0, -197.0, 13.0]) {
															rotate(a = [180, 0, 0]) {
																difference() {
																	union() {
																		translate(v = [-2.5, -12.0, 0.5]) {
																			cube(size = [8.0, 12.0, 12.0]);
																		}
																		translate(v = [-2.5, -0.05, 4.0]) {
																			cube(size = [5.0, 3.0, 5.0]);
																		}
																	}
																	union() {
																		translate(v = [0, -7.0, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				difference() {
																					union() {
																						translate(v = [-20.0, -3.4619999999999997, 0]) {
																							cube(size = [20, 6.9239999999999995, 3]);
																						}
																						linear_extrude(height = 3) {
																							polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
																						}
																					}
																					union();
																				}
																			}
																		}
																		translate(v = [0, 3.0500000000000003, 6.5]) {
																			rotate(a = [90, 0, 0]) {
																				cylinder(h = 22.95, r = 1.8);
																			}
																		}
																	}
																}
															}
														}
														translate(v = [-2.5, -196.8, 11.5]) {
															cube(size = [8.0, 196.6, 3.0]);
														}
														translate(v = [-2.5, -100.0, 14.45]) {
															cube(size = [12.0, 3.0, 6.05]);
														}
													}
													union();
												}
											}
										}
									}
									union();
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [44.65, -21.25, -2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-0.35, 0, 0]) {
											hull() {
												translate(v = [-4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [-4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
											}
										}
										translate(v = [-2.5, -2.5, 2.35]) {
											cube(size = [5.0, 5.0, 3.0]);
										}
									}
									union() {
										translate(v = [0, 0, 0]) {
											rotate(a = [0, 180, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.8);
														}
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [-1.5, -3.0, 2.4]) {
											cube(size = [3.0, 6.0, 3.0500000000000003]);
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[-2.7, 4.75], [-1.9, 5.55], [-2.7, 5.55]]);
												}
											}
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[2.7, 4.75], [1.9, 5.55], [2.7, 5.55]]);
												}
											}
										}
										translate(v = [-4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [-4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
									}
								}
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [44.65, -21.25, 211.4]) {
			rotate(a = [180, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-0.35, 0, 0]) {
											hull() {
												translate(v = [-4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [-4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
											}
										}
										translate(v = [-2.5, -2.5, 2.35]) {
											cube(size = [5.0, 5.0, 3.0]);
										}
									}
									union() {
										translate(v = [0, 0, 0]) {
											rotate(a = [0, 180, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.8);
														}
														translate(v = [0, 0, -20.0]) {
															cylinder(h = 20.0, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [-1.5, -3.0, 2.4]) {
											cube(size = [3.0, 6.0, 3.0500000000000003]);
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[-2.7, 4.75], [-1.9, 5.55], [-2.7, 5.55]]);
												}
											}
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[2.7, 4.75], [1.9, 5.55], [2.7, 5.55]]);
												}
											}
										}
										translate(v = [-4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [-4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
									}
								}
							}
						}
					}
					union();
				}
			}
		}
	}
	union();
}
