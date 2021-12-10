import LHR.toolbox


if __name__ == "__main__":
      _dict={
            "name":"LHR",
            "age":24,
            "nike name":"every is ok"
      }


      _check_list=[
            None,
            [age for age in range(0,100)],
            None
      ]

      LHR.toolbox.print_dict(_dict)
      print(_check_list)
      print(LHR.toolbox.CheckDictCorrect(_dict,_check_list))
      