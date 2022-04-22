



<ModalHeader toggle={toggle}>ServiceProviders Item</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="ServiceProviders-name">Full Name</Label>
              <Input
                type="text"
                id="ServiceProviders-name"
                name="name"
                defaultvalue={this.state.activeItem.fullNameSP}
                onChange={this.handleChange}
                placeholder="Enter ServiceProviders Full Name"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-cnic">CNIC Number</Label>
              <Input
                type="text"
                id="ServiceProviders-cnic"
                name="cnic"
                defaultvalue={this.state.activeItem.cnicSP}
                onChange={this.handleChange}
                placeholder="42201-3748392-7"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-address">Address</Label>
              <Input
                type="text"
                id="ServiceProviders-address"
                name="address"
                defaultvalue={this.state.activeItem.addressSP}
                onChange={this.handleChange}
                placeholder="A-245, Block-5, Gulshan-e-Iqbal"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-city">City</Label>
              <Input
                type="text"
                id="ServiceProviders-city"
                name="city"
                defaultvalue={this.state.activeItem.citySP}
                onChange={this.handleChange}
                placeholder="Karachi"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-date">Date of Birth</Label>
              <Input
                type="date"
                id="ServiceProviders-dob"
                name="dob"
                defaultvalue={this.state.activeItem.dobSP}
                onChange={this.handleChange}
                placeholder="07/12/1999"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-Language">Language</Label>
              <Input
                type="text"
                id="ServiceProviders-Language"
                name="Language"
                defaultvalue={this.state.activeItem.languageSP}
                onChange={this.handleChange}
                placeholder="Urdu or English"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        
        <ModalHeader toggle={toggle}>Booking Item</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="Booking-date">date</Label>
              <Input
                type="date"
                id="Booking-date"
                name="date"
                defaultvalue={this.state.activeItem.bookingDate}
                onChange={this.handleChange}
                placeholder="Enter Booking date"
              />
            </FormGroup>
            <FormGroup>
              <Label for="Booking-slot">CNIC Number</Label>
              <Input
                type="text"
                id="Booking-slot"
                name="slot"
                defaultvalue={this.state.activeItem.bookingSlot}
                onChange={this.handleChange}
                placeholder="12:30"
              />
            </FormGroup>
            <FormGroup>
              <Label for="Booking-Service type">service type</Label>
              <Input
                type="text"
                id="Booking-Service type"
                name="Service type"
                defaultvalue={this.state.activeItem.serviceType}
                onChange={this.handleChange}
                placeholder="cleaning"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-ID">Service Provider ID</Label>
              <Input
                type="text"
                id="ServiceProviders-ID"
                name="ID"
                defaultvalue={this.state.activeItem.ServiceProviderID}
                onChange={this.handleChange}
                placeholder="11111"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        

        <ModalHeader toggle={toggle}>Listing Item</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="Charges">Charges</Label>
              <Input
                type="text"
                id="Charges"
                name="Charges"
                defaultvalue={this.state.activeItem.Charges}
                onChange={this.handleChange}
                placeholder="Enter Charges"
              />
            </FormGroup>
          </Form>
        </ModalBody>