const DATA = {
 "options": [
  {
   "key": "current",
   "title": "Current (v2)",
   "note": "Linear in L, step 0.1086. Background = dark3.",
   "param": [
    "step",
    0.1086
   ],
   "bg": "dark3",
   "bgHex": "#001901",
   "bgL": 0.1742,
   "ramp": {
    "dark4": {
     "l": 0.0656,
     "hex": "#000300"
    },
    "dark3": {
     "l": 0.1742,
     "hex": "#001901"
    },
    "dark2": {
     "l": 0.2828,
     "hex": "#00360c"
    },
    "dark1": {
     "l": 0.3914,
     "hex": "#005522"
    },
    "base": {
     "l": 0.5,
     "hex": "#2b7440"
    },
    "light1": {
     "l": 0.6086,
     "hex": "#4d955f"
    },
    "light2": {
     "l": 0.7172,
     "hex": "#6fb77f"
    },
    "light3": {
     "l": 0.8258,
     "hex": "#91daa0"
    },
    "light4": {
     "l": 0.9344,
     "hex": "#b4ffc3"
    }
   },
   "standards": {
    "aa": {
     "row": "light1",
     "bar": 4.5,
     "fg": "#4d955f",
     "accents": {
      "yellow-orange": "#b27238",
      "yellow": "#9c7f26",
      "yellow-green": "#7a8c3a",
      "green": "#4d955f",
      "cyan": "#039885",
      "blue-cyan": "#0094a7",
      "blue": "#3a8bbe",
      "blue-violet": "#697fc5",
      "violet": "#8d73bb",
      "magenta": "#a869a2",
      "grey": "#838383"
     },
     "contrast": {
      "yellow-orange": 4.7,
      "yellow": 4.81,
      "yellow-green": 4.95,
      "green": 5.07,
      "cyan": 5.12,
      "blue-cyan": 5.08,
      "blue": 4.93,
      "blue-violet": 4.78,
      "violet": 4.65,
      "magenta": 4.57,
      "grey": 4.86
     },
     "worst": {
      "hue": "magenta",
      "ratio": 4.57
     }
    },
    "aaa": {
     "row": "light2",
     "bar": 7.0,
     "fg": "#6fb77f",
     "accents": {
      "yellow-orange": "#d69359",
      "yellow": "#bea04b",
      "yellow-green": "#9bae5c",
      "green": "#6fb77f",
      "cyan": "#42baa6",
      "blue-cyan": "#37b6ca",
      "blue": "#5dade2",
      "blue-violet": "#89a0e9",
      "violet": "#ae94de",
      "magenta": "#cb8ac5",
      "grey": "#a4a4a4"
     },
     "contrast": {
      "yellow-orange": 7.18,
      "yellow": 7.3,
      "yellow-green": 7.55,
      "green": 7.68,
      "cyan": 7.73,
      "blue-cyan": 7.64,
      "blue": 7.5,
      "blue-violet": 7.26,
      "violet": 7.1,
      "magenta": 7.0,
      "grey": 7.39
     },
     "worst": {
      "hue": "magenta",
      "ratio": 7.0
     }
    }
   },
   "brights": {
    "aa": {
     "yellow-orange": "#d69359",
     "yellow": "#bea04b",
     "yellow-green": "#9bae5c",
     "green": "#6fb77f",
     "cyan": "#42baa6",
     "blue-cyan": "#37b6ca",
     "blue": "#5dade2",
     "blue-violet": "#89a0e9",
     "violet": "#ae94de",
     "magenta": "#cb8ac5",
     "grey": "#a4a4a4"
    },
    "aaa": {
     "yellow-orange": "#fbb57b",
     "yellow": "#e2c36e",
     "yellow-green": "#bdd17e",
     "green": "#91daa0",
     "cyan": "#6addc9",
     "blue-cyan": "#62d9ed",
     "blue": "#80d0ff",
     "blue-violet": "#aac3ff",
     "violet": "#d1b6ff",
     "magenta": "#eface8",
     "grey": "#c6c6c6"
    }
   }
  },
  {
   "key": "b",
   "title": "B \u2014 Eleven steps",
   "note": "Linear in L with 5 steps either side of base. The background moves to dark4 of the finer ramp; AA accents sit at light2, AAA at light3.",
   "param": [
    "step",
    0.0762
   ],
   "bg": "dark4",
   "bgHex": "#001e02",
   "bgL": 0.1952,
   "ramp": {
    "dark5": {
     "l": 0.119,
     "hex": "#000c00"
    },
    "dark4": {
     "l": 0.1952,
     "hex": "#001e02"
    },
    "dark3": {
     "l": 0.2714,
     "hex": "#00330c"
    },
    "dark2": {
     "l": 0.3476,
     "hex": "#004916"
    },
    "dark1": {
     "l": 0.4238,
     "hex": "#0d5e2b"
    },
    "base": {
     "l": 0.5,
     "hex": "#2b7440"
    },
    "light1": {
     "l": 0.5762,
     "hex": "#438b55"
    },
    "light2": {
     "l": 0.6524,
     "hex": "#5ba36b"
    },
    "light3": {
     "l": 0.7286,
     "hex": "#72bb82"
    },
    "light4": {
     "l": 0.8048,
     "hex": "#8ad399"
    },
    "light5": {
     "l": 0.881,
     "hex": "#a2edb1"
    }
   },
   "standards": {
    "aa": {
     "row": "light2",
     "bar": 4.5,
     "fg": "#5ba36b",
     "accents": {
      "yellow-orange": "#c17f45",
      "yellow": "#aa8c36",
      "yellow-green": "#879a48",
      "green": "#5ba36b",
      "cyan": "#25a592",
      "blue-cyan": "#13a2b5",
      "blue": "#4898cc",
      "blue-violet": "#768cd3",
      "violet": "#9a80c9",
      "magenta": "#b676b0",
      "grey": "#909090"
     },
     "contrast": {
      "yellow-orange": 5.38,
      "yellow": 5.49,
      "yellow-green": 5.69,
      "green": 5.81,
      "cyan": 5.79,
      "blue-cyan": 5.78,
      "blue": 5.59,
      "blue-violet": 5.45,
      "violet": 5.31,
      "magenta": 5.23,
      "grey": 5.54
     },
     "worst": {
      "hue": "magenta",
      "ratio": 5.23
     }
    },
    "aaa": {
     "row": "light3",
     "bar": 7.0,
     "fg": "#72bb82",
     "accents": {
      "yellow-orange": "#da965d",
      "yellow": "#c2a44f",
      "yellow-green": "#9eb25f",
      "green": "#72bb82",
      "cyan": "#46beaa",
      "blue-cyan": "#3cbacd",
      "blue": "#61b0e5",
      "blue-violet": "#8ca4ed",
      "violet": "#b297e2",
      "magenta": "#ce8ec8",
      "grey": "#a7a7a7"
     },
     "contrast": {
      "yellow-orange": 7.17,
      "yellow": 7.35,
      "yellow-green": 7.57,
      "green": 7.71,
      "cyan": 7.76,
      "blue-cyan": 7.67,
      "blue": 7.46,
      "blue-violet": 7.29,
      "violet": 7.09,
      "magenta": 7.02,
      "grey": 7.36
     },
     "worst": {
      "hue": "magenta",
      "ratio": 7.02
     }
    }
   },
   "brights": {
    "aa": {
     "yellow-orange": "#da965d",
     "yellow": "#c2a44f",
     "yellow-green": "#9eb25f",
     "green": "#72bb82",
     "cyan": "#46beaa",
     "blue-cyan": "#3cbacd",
     "blue": "#61b0e5",
     "blue-violet": "#8ca4ed",
     "violet": "#b297e2",
     "magenta": "#ce8ec8",
     "grey": "#a7a7a7"
    },
    "aaa": {
     "yellow-orange": "#f4ae75",
     "yellow": "#dbbc68",
     "yellow-green": "#b6ca77",
     "green": "#8ad399",
     "cyan": "#62d7c2",
     "blue-cyan": "#5ad3e6",
     "blue": "#79c9ff",
     "blue-violet": "#a4bcff",
     "violet": "#caaffc",
     "magenta": "#e8a5e1",
     "grey": "#bfbfbf"
    }
   }
  },
  {
   "key": "c",
   "title": "C \u2014 Melodic (asymmetric)",
   "note": "Dark side compressed (step 0.0950) to lift the background; light side stretched the minimum (step 0.1259) so AA and AAA still hold at the familiar light1 / light2 rows.",
   "param": [
    "light step",
    0.1259,
    "dark step",
    0.095
   ],
   "bg": "dark3",
   "bgHex": "#002305",
   "bgL": 0.215,
   "ramp": {
    "dark4": {
     "l": 0.12,
     "hex": "#000c00"
    },
    "dark3": {
     "l": 0.215,
     "hex": "#002305"
    },
    "dark2": {
     "l": 0.31,
     "hex": "#003e0f"
    },
    "dark1": {
     "l": 0.405,
     "hex": "#035926"
    },
    "base": {
     "l": 0.5,
     "hex": "#2b7440"
    },
    "light1": {
     "l": 0.6259,
     "hex": "#529a64"
    },
    "light2": {
     "l": 0.7518,
     "hex": "#79c289"
    },
    "light3": {
     "l": 0.8777,
     "hex": "#a1ecb0"
    },
    "light4": {
     "l": 1.0036,
     "hex": "#ffffff"
    }
   },
   "standards": {
    "aa": {
     "row": "light1",
     "bar": 4.5,
     "fg": "#529a64",
     "accents": {
      "yellow-orange": "#b8773d",
      "yellow": "#a2842c",
      "yellow-green": "#7f913f",
      "green": "#529a64",
      "cyan": "#159d8a",
      "blue-cyan": "#0099ac",
      "blue": "#4090c3",
      "blue-violet": "#6e84cb",
      "violet": "#9278c0",
      "magenta": "#ad6fa7",
      "grey": "#888888"
     },
     "contrast": {
      "yellow-orange": 4.62,
      "yellow": 4.73,
      "yellow-green": 4.85,
      "green": 4.96,
      "cyan": 5.01,
      "blue-cyan": 4.95,
      "blue": 4.82,
      "blue-violet": 4.69,
      "violet": 4.56,
      "magenta": 4.51,
      "grey": 4.77
     },
     "worst": {
      "hue": "magenta",
      "ratio": 4.51
     }
    },
    "aaa": {
     "row": "light2",
     "bar": 7.0,
     "fg": "#79c289",
     "accents": {
      "yellow-orange": "#e29d64",
      "yellow": "#caab57",
      "yellow-green": "#a5b966",
      "green": "#79c289",
      "cyan": "#4fc5b1",
      "blue-cyan": "#46c1d5",
      "blue": "#68b8ed",
      "blue-violet": "#93abf5",
      "violet": "#b99eea",
      "magenta": "#d695d0",
      "grey": "#aeaeae"
     },
     "contrast": {
      "yellow-orange": 7.44,
      "yellow": 7.62,
      "yellow-green": 7.83,
      "green": 7.96,
      "cyan": 8.01,
      "blue-cyan": 7.93,
      "blue": 7.78,
      "blue-violet": 7.55,
      "violet": 7.36,
      "magenta": 7.3,
      "grey": 7.62
     },
     "worst": {
      "hue": "magenta",
      "ratio": 7.3
     }
    }
   },
   "brights": {
    "aa": {
     "yellow-orange": "#e29d64",
     "yellow": "#caab57",
     "yellow-green": "#a5b966",
     "green": "#79c289",
     "cyan": "#4fc5b1",
     "blue-cyan": "#46c1d5",
     "blue": "#68b8ed",
     "blue-violet": "#93abf5",
     "violet": "#b99eea",
     "magenta": "#d695d0",
     "grey": "#aeaeae"
    },
    "aaa": {
     "yellow-orange": "#ffc895",
     "yellow": "#f3d47f",
     "yellow-green": "#cde28e",
     "green": "#a1ecb0",
     "cyan": "#7cefd9",
     "blue-cyan": "#74ebff",
     "blue": "#abdeff",
     "blue-violet": "#c5d4ff",
     "violet": "#dfc9ff",
     "magenta": "#ffbdf9",
     "grey": "#d7d7d7"
    }
   }
  },
  {
   "key": "a",
   "title": "A \u2014 Compressed nine",
   "note": "Every step pulled toward base by the same factor (~0.83x); AA accents move to light2, AAA to light3, so the contrast bars still hold. Maximum pull toward base.",
   "param": [
    "step",
    0.087
   ],
   "bg": "dark3",
   "bgHex": "#002909",
   "bgL": 0.239,
   "ramp": {
    "dark4": {
     "l": 0.152,
     "hex": "#001300"
    },
    "dark3": {
     "l": 0.239,
     "hex": "#002909"
    },
    "dark2": {
     "l": 0.326,
     "hex": "#004211"
    },
    "dark1": {
     "l": 0.413,
     "hex": "#075b28"
    },
    "base": {
     "l": 0.5,
     "hex": "#2b7440"
    },
    "light1": {
     "l": 0.587,
     "hex": "#468e58"
    },
    "light2": {
     "l": 0.674,
     "hex": "#61a972"
    },
    "light3": {
     "l": 0.761,
     "hex": "#7cc58c"
    },
    "light4": {
     "l": 0.848,
     "hex": "#98e2a7"
    }
   },
   "standards": {
    "aa": {
     "row": "light2",
     "bar": 4.5,
     "fg": "#61a972",
     "accents": {
      "yellow-orange": "#c8854c",
      "yellow": "#b1933d",
      "yellow-green": "#8ea04e",
      "green": "#61a972",
      "cyan": "#30ac99",
      "blue-cyan": "#22a8bc",
      "blue": "#4f9fd3",
      "blue-violet": "#7c93da",
      "violet": "#a186d0",
      "magenta": "#bd7db7",
      "grey": "#969696"
     },
     "contrast": {
      "yellow-orange": 5.23,
      "yellow": 5.38,
      "yellow-green": 5.52,
      "green": 5.62,
      "cyan": 5.67,
      "blue-cyan": 5.6,
      "blue": 5.47,
      "blue-violet": 5.33,
      "violet": 5.17,
      "magenta": 5.13,
      "grey": 5.37
     },
     "worst": {
      "hue": "magenta",
      "ratio": 5.13
     }
    },
    "aaa": {
     "row": "light3",
     "bar": 7.0,
     "fg": "#7cc58c",
     "accents": {
      "yellow-orange": "#e5a067",
      "yellow": "#ccae5a",
      "yellow-green": "#a8bc69",
      "green": "#7cc58c",
      "cyan": "#53c8b4",
      "blue-cyan": "#4ac4d8",
      "blue": "#6bbbf0",
      "blue-violet": "#96aef8",
      "violet": "#bca1ed",
      "magenta": "#d998d3",
      "grey": "#b1b1b1"
     },
     "contrast": {
      "yellow-orange": 7.23,
      "yellow": 7.4,
      "yellow-green": 7.62,
      "green": 7.74,
      "cyan": 7.79,
      "blue-cyan": 7.7,
      "blue": 7.56,
      "blue-violet": 7.35,
      "violet": 7.16,
      "magenta": 7.1,
      "grey": 7.41
     },
     "worst": {
      "hue": "magenta",
      "ratio": 7.1
     }
    }
   },
   "brights": {
    "aa": {
     "yellow-orange": "#e5a067",
     "yellow": "#ccae5a",
     "yellow-green": "#a8bc69",
     "green": "#7cc58c",
     "cyan": "#53c8b4",
     "blue-cyan": "#4ac4d8",
     "blue": "#6bbbf0",
     "blue-violet": "#96aef8",
     "violet": "#bca1ed",
     "magenta": "#d998d3",
     "grey": "#b1b1b1"
    },
    "aaa": {
     "yellow-orange": "#ffbc82",
     "yellow": "#e9ca76",
     "yellow-green": "#c4d885",
     "green": "#98e2a7",
     "cyan": "#72e5d0",
     "blue-cyan": "#6ae1f5",
     "blue": "#92d6ff",
     "blue-violet": "#b6caff",
     "violet": "#d8bdff",
     "magenta": "#f6b3ef",
     "grey": "#cdcdcd"
    }
   }
  }
 ],
 "roles": {
  "comment": {
   "colour": "grey",
   "style": "italic"
  },
  "keyword": {
   "colour": "cyan"
  },
  "tag": {
   "colour": "cyan"
  },
  "jsonKey": {
   "colour": "cyan"
  },
  "heading": {
   "colour": "cyan"
  },
  "cssClassName": {
   "colour": "cyan"
  },
  "string": {
   "colour": "yellow-green"
  },
  "function": {
   "colour": "blue"
  },
  "attribute": {
   "colour": "blue"
  },
  "cssPropertyName": {
   "colour": "blue"
  },
  "link": {
   "colour": "blue"
  },
  "type": {
   "colour": "blue-cyan"
  },
  "class": {
   "colour": "blue-cyan"
  },
  "embedDelimiter": {
   "colour": "blue-cyan"
  },
  "identifier": {
   "colour": "blue-cyan"
  },
  "variable": {
   "colour": "yellow"
  },
  "regex": {
   "colour": "yellow"
  },
  "decorator": {
   "colour": "yellow",
   "style": "italic"
  },
  "number": {
   "colour": "yellow-orange"
  },
  "constant": {
   "colour": "yellow-orange"
  },
  "matchHighlight": {
   "colour": "yellow-orange"
  },
  "punctuation": {
   "colour": "grey"
  },
  "operator": {
   "colour": "grey"
  },
  "error": {
   "colour": "magenta"
  },
  "invalid": {
   "colour": "magenta"
  },
  "deleted": {
   "colour": "magenta"
  },
  "inserted": {
   "colour": "green"
  },
  "linkHover": {
   "colour": "blue-violet"
  },
  "inlineCode": {
   "colour": "violet"
  },
  "pseudoClass": {
   "colour": "violet"
  }
 },
 "v2step": 0.1086
};
