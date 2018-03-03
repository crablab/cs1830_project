import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class SpriteSheetTemplate:
    ##self.image = None
    ##self.name_to_sprite_list = {}

    def draw(self, canvas, pos, sprite_name, scale):
        """
        canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)

        image               = self.image
        center_source       = self.name_to_sprite_list[sprite_name].middle_pos
        width_height_source = (self.name_to_sprite_list[sprite_name].width,
                               self.name_to_sprite_list[sprite_name].height)
        center_dest         = pos
        width_height_dest   = (self.name_to_sprite_list[sprite_name].width*scale,
                               self.name_to_sprite_list[sprite_name].height*scale)
        """
        canvas.draw_image(self.image,
                          self.name_to_sprite_list[sprite_name].pos_middle,
                          (
                              self.name_to_sprite_list[sprite_name].width,
                              self.name_to_sprite_list[sprite_name].height
                          ),
                          pos,
                          (
                              self.name_to_sprite_list[sprite_name].width*scale,
                              self.name_to_sprite_list[sprite_name].height*scale
                          ))
