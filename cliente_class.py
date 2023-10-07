class Cliente:
      def _init_(self, primeiro_nome, ultimo_nome, endereço, número_celular, email, genero):
          self.primeiro_nome = primeiro_nome
          self.ultimo_nome = ultimo_nome
          self.endereço = endereço
          self.número_celular = número_celular
          self.email = email
          self.genero = genero


      def setPrimeiro_nome (self, primeiro_nome):
          self.primeiro_nome = primeiro_nome
      def setUltimo_nome (self, ultimo_nome):
          self.ultimo_nome = ultimo_nome
      def setEndereço (self, endereço):
          self.endereço = endereço
      def setNúmero_celular (self, número_celular):
          self.número_celular = número_celular
      def setEmail (self, email):
          self.email = email
      def setGenero (self, genero):
          self.genero = genero


      def getPrimeiro_nome (self):
          return self.primeiro_nome
      def getUltimo_nome (self):
          return self.ultimo_nome       
      def getEndereço (self):
          return self.endereço
      def getNúmero_celular (self):
          return self.número_celular
      def getEmail (self):
          return self.email
      def getGenero (self):
          return self.genero
        